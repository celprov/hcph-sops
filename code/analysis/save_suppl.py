import json

## Helper function to save figure captions
def save_caption(caption, save_layout, entities):
    """
    Save the figure caption to a JSON file.
    
    Parameters:
    - caption: The caption text to save.
    - save_layout: A BIDSLayout object for saving the caption.
    - entities: A dictionary containing BIDS entities for the filename.
    """
    # Update the entities to use .json extension
    entities['extension'] = '.json'
    json_save_path = save_layout.build_path(entities, validate=False)

    # Save the caption to a JSON file
    caption_data = {"caption": caption}
    with open(json_save_path, 'w') as json_file:
        json.dump(caption_data, json_file)