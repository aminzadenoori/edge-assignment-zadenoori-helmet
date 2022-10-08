def convert_infr_time_to_fps(infr_time: float) -> int:
    # Gets the time of inference (infr_time) and returns Frames Per Second (fps)
    fps = int(1.0 / infr_time)
    return fps
