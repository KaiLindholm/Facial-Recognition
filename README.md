# Facial-Recognition
Using OpenCv, PyTorch and other libraries the goal of this project is to create a facial recognition algorithm to streamline taking attendance at chapter. 

The Facial Recognition Problem: 
    Face Detection: This project will detect and isolate images. With images with multiple faces they will each be detected individually
    Face Recognition: After detecting each individual face, it then will be ran through the Neural Network for classification 

Face Detection Approach: 
    Using the Haar Cascades: 
        Using the key rules that 1) The area of the eye is darker than the forehead and the cheeks
                                 2) The area of the nose is brighter than the eyes. 
    Since an image will not usually contain a face in every corner of the image. The Cascades classifier uses progressively more complex Haar features as it detects parts of the image with more face in it. 

    Issues: 
        To improve performace multithreading for the camera will be added. 

Face Recognition: 
    Problems: 1) The dataset is much smaller than in my previous project, where it had tens of thouands of images     to train on. 