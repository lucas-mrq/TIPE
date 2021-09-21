## The code
For this code I chose to separate the process into 3 sub-codes as each one takes a long time to run. The script has several steps which I will explain.

The starting image is as follows:
<p align="center"><img src="0_groix_initialPicture.jpg" width="500" ></p align="center">
  
<p align="center"><img src="arrowExemple/0_arrow_initialPicture.jpg" width="500" ></p align="center">

To start I chose to change the images to separate arrows, land and water (navy blue, cyan and brown). 
<p align="center"><img src="1_groix_firstProcessing.bmp" width="500" ></p align="center">
  
<p align="center"><img src="arrowExemple/1_arrow_firstProcessing.bmp" width="500" ></p align="center">

However this treatment is not perfect and elements of each colour slip into the wrong place so I then process the image several times to get the one below:
<p align="center"><img src="3_groix_thirdProcessing.bmp" width="500" ></p align="center">
  
<p align="center"><img src="arrowExemple/3_arrow_secondProcessing.bmp" width="500" ></p align="center">

In order to detect the direction of the arrows I try to find the barycentres of the arrows which give us an image with white arrows and a red dot on the barycentre.
<p align="center"><img src="5_groix_arrow_barycenter.bmp" width="500" ></p align="center">
  
<p align="center"><img src="arrowExemple/5_arrow_barycenter.bmp" width="500" ></p align="center">

Finally I look for the largest diagonal passing through each barycentre which gives us its blue arrows with two red dots representing the direction of the vector. The navy blue is then replaced by cyan blue.
<p align="center"><img src="7_groix_secondArrowProcessing.bmp" width="500" ></p align="center">
  
<p align="center"><img src="arrowExemple/7_groix_secondArrowProcessing.bmp" width="500" ></p align="center">

Finally I look for each point in the water for the closest direction and this gives us a map filled with areas with different directions that we can recognise by the shade of green in it.
<p align="center"><img src="8_groix_thirdArrowProcessing.bmp" width="500" ></p align="center">
  
<p align="center"><img src="arrowExemple/8_groix_thirdArrowProcessing.bmp" width="500" ></p align="center">

All that has to be done is to release the particles to obtain our microparticle displacement.
<p align="center"><img src="9_Result.bmp" width="500" ></p align="center">
