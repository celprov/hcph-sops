# Copyright 2025 The Axon Lab <theaxonlab@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# We support and encourage derived works from this project, please read
# about our expectations at
#
#     https://www.nipreps.org/community/licensing/
#
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