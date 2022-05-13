def isCompactCar(img) :
    compact_model ='compactcar.h5'
    model = tf.keras.models.load_model(compact_model, compile=False)
    # 먼저 들어온 이미지 정규화
    preprocessed = preprocessing(img)
    # 분류
    prediction = model.predict(preprocessed)
    # 첫번째 라벨은 경차 두번째라벨은 Ohter
    if prediction[0,0] > prediction[0,1] :
        print("할인 대상 차량 : 경차")
        return 1
    else :
        return 0

def preprocessing(img):
    
    size = (224, 224)
    frame_resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    
    # 이미지 정규화
    # astype : 속성
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1

    # 이미지 차원 재조정 - 예측을 위해 reshape 해줍니다.
    # keras 모델에 공급할 올바른 모양의 배열 생성
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))
    #print(frame_reshaped)
    return frame_reshaped
