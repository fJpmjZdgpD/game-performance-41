def calculate_fps(frames, time):
    if time > 0:
        return frames / time
    return 0

def optimize_resources(resources):
    optimized_resources = []
    for resource in resources:
        if resource.is_active():
            optimized_resources.append(resource)
    return optimized_resources

def load_assets(asset_list):
    loaded_assets = {}
    for asset in asset_list:
        loaded_assets[asset.name] = asset.load()
    return loaded_assets

def unload_assets(asset_dict):
    for asset_name, asset in asset_dict.items():
        asset.unload()

def frame_time_logging(frame_time):
    import logging
    logging.info(f'Frame time: {frame_time} ms')

def get_delta_time(last_time, current_time):
    return current_time - last_time