#include <opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include <iostream>
using namespace cv;


int main()
{
    Mat test = imread("C:\\Users\\tuyue\\source\\repos\\pork_cv\\pork_cv\\data\\pork.jpg");
    int center_x = test.cols / 2;
    int center_y = test.rows / 2;
    Mat cut_test = test(Range(center_y - 400, center_y + 400), Range(center_x - 400, center_x + 400));
    imshow("cut", cut_test);
    waitKey(6000);
    return 0;
}
