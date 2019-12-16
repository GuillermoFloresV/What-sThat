from imageai.Detection import ObjectDetection
import os

inputted_image = input("Type the name of your image: ")

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(
    os.path.join(
        execution_path,
        "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections, extracted_images = detector.detectObjectsFromImage(
    input_image=os.path.join(
        execution_path, inputted_image), output_image_path=os.path.join(
            execution_path, "new.jpeg"), extract_detected_objects=True)

# Maybe do a dictionary at the same time in order to count them and
# display to the user how many times it saw a certain item. (maybe make
# the text file downloadable as well as a download link of the extracted
# images)
list_of_items_found = []
percentage_probability_of_item = []

for eachObject in detections:
    #    print(eachObject["name"] , " : " , eachObject["percentage_probability"])
    list_of_items_found.append(eachObject["name"])
    percentage_probability_of_item.append(eachObject["percentage_probability"])

#makes everything into a dictionary in order for better user readability (give code better formatting with object and the object percentage probability)
my_dict = dict(zip(list_of_items_found, percentage_probability_of_item))


#if the length of items found is greater than 0, then print out the dictionary to the user, else, let them know that the script found nothing and the program ends.
if len(list_of_items_found) > 0:
    print(my_dict)
else:
    print("Sorry, we could not find any items in this picture. Please try another image.")
