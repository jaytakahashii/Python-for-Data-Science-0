import sys
from typing import Generator, Iterable
import time
import shutil

# Fixed width estimation for components of the status text.
WIDTH_PERCENT = 4          # e.g., "100%"
WIDTH_BRACKETS = 3         # e.g., "|[ ]|"
# e.g., " [00:00<00:00, 100.00it/s]" (Constant length)
WIDTH_TIME_INFO = 30
WIDTH_SPACING = 1          # Space before the counter

# The minimal length the bar is allowed to be.
MIN_BAR_LENGTH = 10


def ft_tqdm(lst: Iterable) -> Generator:
    """
    A simple implementation of a TQDM-like progress bar generator.
    It maximizes the use of the terminal width for the progress bar
    while ensuring clean line updates and responsive display.

    Args:
        lst (Iterable): The iterable object to track (must support len()).

    Yields:
        The current item from the iterable.
    """
    # ----------------------------------------------
    # 1. Initial setup and width calculation
    # ----------------------------------------------

    try:
        # Get terminal width or fallback to 80
        columns = shutil.get_terminal_size().columns
    except Exception:
        columns = 80  # Default to 80 if not TTY

    try:
        total = len(lst)
    except TypeError:
        print("Error: ft_tqdm requires a sized iterable (like range, list, tuple).", file=sys.stderr)
        return

    start_time = time.time()
    count = 0

    # Calculate the maximum width of the counter (e.g., " 1000/1000")
    # This must be calculated dynamically based on 'total' to ensure full width utilization.
    counter_max_width = len(f"{total}/{total}") + WIDTH_SPACING

    # Determine if we have enough space for the full (time-inclusive) display
    MIN_FULL_WIDTH = WIDTH_PERCENT + WIDTH_BRACKETS + \
        counter_max_width + WIDTH_TIME_INFO + MIN_BAR_LENGTH

    use_full_display = columns >= MIN_FULL_WIDTH

    if use_full_display:
        # Full display: use the rest of the space for the bar
        fixed_width_total = WIDTH_PERCENT + WIDTH_BRACKETS + \
            counter_max_width + WIDTH_TIME_INFO
        BAR_LENGTH = max(MIN_BAR_LENGTH, columns - fixed_width_total)
    else:
        # Basic display (no time info): use the rest of the space for the bar
        fixed_width_basic = WIDTH_PERCENT + WIDTH_BRACKETS + counter_max_width
        BAR_LENGTH = max(MIN_BAR_LENGTH, columns - fixed_width_basic)

        # Fallback for extremely narrow terminals (ensure BAR_LENGTH >= 1)
        if BAR_LENGTH < 1:
            remaining_space = columns - \
                (WIDTH_PERCENT + WIDTH_BRACKETS + counter_max_width)
            BAR_LENGTH = max(1, remaining_space)

    # ----------------------------------------------
    # 2. Time formatting and line writing helpers
    # ----------------------------------------------

    def _format_time(seconds: float) -> str:
        """Formats time in seconds into MM:SS string."""
        if seconds < 0:
            return "??:??"
        m, s = divmod(int(seconds), 60)
        return f"{m:02}:{s:02}"

    def _write_line(output_str: str, new_line: bool = False):
        """
        Pads the output string with spaces up to the terminal width (columns)
        to clear the rest of the line, preventing display artifacts.
        """
        # Calculate padding needed to clear the entire line
        padding_needed = max(0, columns - len(output_str))

        # Write carriage return, the output string, and the padding
        sys.stdout.write('\r' + output_str + (' ' * padding_needed))

        # Add a newline only if requested (for finalization)
        if new_line:
            sys.stdout.write('\n')

        sys.stdout.flush()

    # Initial display (0%)
    # Use spaces for the bar and ensure time info is included if using full display
    initial_time_info = f" [{_format_time(0)}<{_format_time(0)}, 0.00it/s]" if use_full_display else ""
    initial_output = (
        f"  0%"
        f"|[{' ' * BAR_LENGTH}]|"
        f" 0/{total}"
        f"{initial_time_info}"
    )
    _write_line(initial_output, new_line=False)

    # ----------------------------------------------
    # 3. Main iteration loop
    # ----------------------------------------------

    for item in lst:
        count += 1
        current_time = time.time()
        elapsed_time = current_time - start_time

        # Set a small minimum time to prevent division by zero for speed calculation
        if elapsed_time < 0.001:
            elapsed_time = 0.001

        percent = count / total
        filled_len = int(BAR_LENGTH * percent)

        # Bar visualization part
        bar = '=' * filled_len
        if filled_len < BAR_LENGTH:
            bar += '>'  # Progress indicator head
        bar += ' ' * (BAR_LENGTH - len(bar))  # Unfilled part

        # Time and speed calculation (only if space allows)
        time_info_str = ""
        if use_full_display:
            it_per_sec = count / elapsed_time
            elapsed_formatted = _format_time(elapsed_time)

            # Estimated Time of Arrival (ETA)
            if it_per_sec > 0:
                eta_seconds = (total - count) / it_per_sec
                eta_formatted = _format_time(eta_seconds)
            else:
                eta_formatted = "??:??"

            time_info_str = f" [{elapsed_formatted}<{eta_formatted}, {it_per_sec:.2f}it/s]"

        # Construct the final output string
        output = (
            f"{int(percent * 100):3d}%"  # Percentage padded to 3 characters
            f"|[{bar}]|"
            f" {count}/{total}"
            f"{time_info_str}"
        )

        # Write the line, clearing any previous remnants
        _write_line(output, new_line=False)

        # Yield the element to the user's code
        yield item

    # ----------------------------------------------
    # 4. Finalization (100% display)
    # ----------------------------------------------

    final_time = time.time()
    final_elapsed_time = final_time - start_time

    # Final display must reflect the full iteration
    final_bar = '=' * BAR_LENGTH

    final_time_info_str = ""
    if use_full_display:
        # Ensure we don't divide by zero for final speed calculation
        if final_elapsed_time < 0.001:
            final_elapsed_time = 0.001

        # Recalculate final speed
        final_it_per_sec = total / final_elapsed_time
        final_elapsed_formatted = _format_time(final_elapsed_time)

        # Final output always shows ETA as 00:00
        final_time_info_str = f" [{final_elapsed_formatted}<00:00, {final_it_per_sec:.2f}it/s]"

    # Final output string
    final_output = (
        f"100%"
        f"|[{final_bar}]|"
        f" {total}/{total}"
        f"{final_time_info_str}"
    )

    # Write the final 100% line and add a newline to complete the display
    _write_line(final_output, new_line=True)
