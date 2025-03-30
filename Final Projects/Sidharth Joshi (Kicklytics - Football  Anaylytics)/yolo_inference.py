from ultralytics import YOLO
model = YOLO('model/best.pt')   #Load model
results = model.predict('input_videos/football1.mp4', save = True)  #Inference on video
print(results[0])  #Print results
print('##########################################')
for box in results[0].boxes:
    print(box)  #Print each box  