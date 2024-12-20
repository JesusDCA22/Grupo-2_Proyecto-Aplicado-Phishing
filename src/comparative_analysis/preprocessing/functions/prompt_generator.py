import re

class PromptGenerator:
    def __init__(self, labels_with_definitions):
        self.labels_with_definitions = labels_with_definitions

    def generate_prompt(self, product):
        labels = [label for label, _ in self.labels_with_definitions]
        definitions = ''.join([f'- {label}: {definition}\n' for label, definition in self.labels_with_definitions])
        prompt = f"""
            You are an assistant specialized in extracting structured information from product descriptions and organizing it into tables.
            Your task is to extract the following information from the product details and label it according to the provided labels: {', '.join(labels)}.
            Each label has the following definition to help guide your extraction:

            {definitions}

            If a label does not have a clear match in the details, complete its value with "null".

            Product information:
            - Details: {product['details']}
            - Description: {product['description']}
            - Category: {product['category']}
            - Characteristics: {product['characteristics']}

            Provide the information in a table with columns corresponding to each label. 
            The table must include **two complete rows**:
            1. The first row contains the label names.
            2. The second row contains the corresponding labeled values.

            Expected response format:
            | {' | '.join(labels)} |
            | {' | '.join(['---'] * len(labels))} |
            | value_1 | value_2 | ... |
            
            Example:
            If the labels are "details", "description", and "category", and the extracted values are 
            "Comfortable sneakers", "Made with recycled materials", and "Footwear", respectively, 
            your response should be:

            | details | description | category |
            | --- | --- | --- |
            | Comfortable sneakers | Made with recycled materials | Footwear |

            Remember:
            - The response must contain two complete rows.
            - Only respond with the table and **do not include additional text**.

            Now, extract and structure the information for the provided product:

            | {' | '.join(labels)} |
            | {' | '.join(['---'] * len(labels))} |
            |
        """
        return prompt.strip()
