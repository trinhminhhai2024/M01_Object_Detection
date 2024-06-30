!git clone https: // github.com/THU-MIG/yolov10.git
%cd yolov10
!pip uninstall - y torch torchvision torchaudio torchtext
!pip install torch torchvision torchaudio torchtext - -extra-index-url https: // download.pytorch.org/whl/cu118
!pip install - q - r requirements.txt
!pip install - e .
!cp / content/drive/MyDrive/yolov10n.pt .
YAML_PATH = '/content/yolov10/Safety_Helmet_Dataset/data.yaml'
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 128
model.train(data=YAML_PATH,
            epochs=EPOCHS,
            batch=BATCH_SIZE,
            imgsz=IMG_SIZE)
