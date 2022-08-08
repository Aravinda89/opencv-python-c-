//Include Libraries
#include<opencv2/opencv.hpp>
#include<iostream>

// Namespace nullifies the use of cv::function(); 
using namespace std;
using namespace cv;

int main() {
	string img_path = "C:\\Users\\yga\\Desktop\25\\C015005282022800163\test_img.jpg";

	// Read an image 
	Mat img_grayscale = imread(img_path, 0);

	// Display the image.
	imshow("grayscale image", img_grayscale);

	// Wait for a keystroke.   
	waitKey(0);

	// Destroys all the windows created                         
	destroyAllWindows();

	return 0;
}
