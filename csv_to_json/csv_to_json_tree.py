import json
from itertools import repeat


class ConvertCsvToJsonTree:
    """
    This class is used to to convert CSV data into json hierarchy tree
    """

    def __init__(self, csv_data):
        """ Initialising class """
        self.max_column = 0
        self.csv_data = csv_data

    def create_parent_tree(self, is_dump_with_indent=True):
        """
        - Find max columns depth in csv 
        - This function is used to create parent tree and push all child into it.
        """
        self.max_column = int(len(self.csv_data.columns) / 3)
        if is_dump_with_indent:
            return json.dumps(self.add_child_to_parent(0, self.csv_data), indent=4)
        else:
            return json.dumps(self.add_child_to_parent(0, self.csv_data))

    def add_child_to_parent(self, level, csv_data):
        """
        - Starts with an empty tree/parent and add levels to the tree/parent
        - Calls mapping_json_encoder function inside map to create n level children levels
        :parameters:
            level - data will be added as per level.
            csv_data - filtered csv_data to be added as per level.
        """
        if level < self.max_column:
            return list(
                filter(None.__ne__, list(
                    map(
                        self.mapping_json_encoder,
                        csv_data.iloc[:, (3 * (level + 1)) - 1].unique(),
                        repeat(level), repeat(csv_data)
                    )
                ))
            )
        else:
            return []

    def mapping_json_encoder(self, level_id, level, csv_data):
        """
        This function is used to create mapping json encoder and add data into n level children tree,
        :parameters:
            level_id - this is refer to be created current level.
            level - data will be added as per level.
            csv_data - filtered csv_data to be added as per level
        """
        csv_data = csv_data[csv_data.iloc[:, 3 * level + 2] == level_id]
        if csv_data.empty:
            return None
        return {
            "label": csv_data.iloc[:, 3 * level + 1].iloc[0].strip(),
            "id": str(int(level_id)).strip(),
            "link": csv_data.iloc[:, 3 * (level + 1)].iloc[0].strip(),
            "children": self.add_child_to_parent((level + 1), csv_data)
        }
