import sys
import time
import shutil


def ft_tqdm(lst: range) -> None:
    """
    A simple implementation of a TQDM-like progress bar generator.
    It maximizes the use of the terminal width for the progress bar
    while ensuring clean line updates and responsive display.

    Args:
        lst (range): An iterable with a known length.

    Yields:
        The current item from the iterable.

    Returns:
        None
    """
    # ----------------------------------------------
    # 1. Initial setup and width calculation
    # ----------------------------------------------
    WIDTH_PERCENT = 4       # e.g., "100%"
    WIDTH_BRACKETS = 4      # e.g., "|[]|"
    WIDTH_TIME_INFO = 26    # e.g., " [00:00<00:00, 100.00it/s]"
    WIDTH_SPACING = 1       # Space before the counter
    MIN_BAR_LENGTH = 5      # e.g., "[====>]"

    try:
        # Get terminal width or fallback to 80
        columns = shutil.get_terminal_size().columns
    except Exception:
        columns = 80  # Default to 80 if not TTY

    try:
        total = len(lst)
    except TypeError:
        print("ft_tqdm requires an iterable with a known length.")
        return

    start_time = time.time()
    count = 0

    # Calculate the maximum width of the counter (e.g., " 1000/1000")
    counter_max_width = WIDTH_SPACING + len(f"{total}/{total}")

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

    # ----------------------------------------------
    # 2. Time formatting and line writing helpers
    # ----------------------------------------------

    def _format_time(seconds: float) -> str:
        """Formats time in seconds into MM:SS string."""
        if seconds < 0:
            return "??:??"
        m, s = divmod(int(seconds), 60)
        return f"{m:02}:{s:02}"

    def _write_line(output_str: str):
        """
        Writes the output string to stdout, clearing any previous content.
        """
        sys.stdout.write('\r' + output_str)
        sys.stdout.flush()

    # Initial display (0%)
    if use_full_display:
        initial_time_info = f" [{_format_time(0)}<{_format_time(0)}, 0.00it/s]"
    else:
        initial_time_info = ""

    initial_output = (
        f"  0%"
        f"|[{' ' * BAR_LENGTH}]|"
        f" 0/{total}"
        f"{initial_time_info}"
    )
    _write_line(initial_output)

    # ----------------------------------------------
    # 3. Main iteration loop
    # ----------------------------------------------

    for item in lst:
        count += 1
        current_time = time.time()
        elapsed_time = current_time - start_time

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

            time_info_str = (
                f" [{elapsed_formatted}<{eta_formatted}"
                f", {it_per_sec:5.2f}it/s]"
            )

        # Construct the final output string
        output = (
            f"{int(percent * 100):3d}%"
            f"|[{bar}]|"
            f" {count}/{total}"
            f"{time_info_str}"
        )

        # Write the line, clearing any previous remnants
        _write_line(output)

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
        final_time_info_str = (
            f" [{final_elapsed_formatted}<00:00"
            f", {final_it_per_sec:5.2f}it/s]"
        )

    # Final output string
    final_output = (
        f"100%"
        f"|[{final_bar}]|"
        f" {total}/{total}"
        f"{final_time_info_str}"
    )

    # Write the final 100% line and add a newline to complete the display
    _write_line(final_output)
