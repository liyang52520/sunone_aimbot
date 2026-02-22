from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("models/YOLOv8s_apex_teammate_enemy.pt")
    model.export(format="openvino", half=True, nms=True)
