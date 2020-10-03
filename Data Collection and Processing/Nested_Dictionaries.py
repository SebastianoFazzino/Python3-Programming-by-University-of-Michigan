#Nested Dictionaries

#given the following list of dictionaries,
#let's say we want to retrieve hair color:
    
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

#we use multime indexing do descend the different layers
color = info['personal_data']['physical_features']['color']['hair']
print(color)

#let' say we want to change a value in the nested dictionaries:
    
info['personal_data']['physical_features']['height'] = "6'1"
new_height = info['personal_data']['physical_features']['height']
print(new_height)