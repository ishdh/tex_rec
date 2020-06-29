#usage: python text_localization.py --image images\example01.jpg/png/jpeg
from pytesseract import Output
import pytesseract 
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
	help="path to input image")
ap.add_argument("-c","--min_confidence", type = float, default = 0.5,
	help = "minimum probability required to inspect a region")
ap.add_argument("-o", "--output", type=str, default="medicine.csv",
	help="path to output CSV file containing medicine's name")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type= Output.DICT)
#csv = open(args["output"], "w")

for i in range(0, len(results["text"])):

	x = results["left"][i]
	y = results["top"][i]
	w = results["width"][i]
	h = results["height"][i]

	text = results["text"][i]
	conf = int(results["conf"][i])

	if conf > args["min_confidence"]:

		print("Confidence: {}".format(conf))
		print("Text: {}".format(text))
		print("")

		text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
		cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)

		#csv.write("{},{}\n".format(text)
	    #csv.flush()

#csv.close()
cv2.imshow("Image", image)
cv2.waitKey(0)		