<h2>Content Based Image Retreival System</h2>
<h5>Brief:</h5>
<p>It is basically a simple image search engine, which retreives the similar images from the database
on the basis of comparison between their features.Two different methods have been implemented for this purpose--</p>
<br>
<p>1.Color Histogram method which compares images on the basis of color similarity between them.</p>
<p>2.ORB feature detection algorithm which matches on the basis of distance between the keypoints.</p>
<h4>Technologies used:</h4>
<ul class="list-style-type:disc">
	<li>Python 2.7</li>
	<li>OpenCv 3.0 for Image processing</li>
	<li>Numpy for mathematical calculations</li>
	<li>Tkinter for GUI</li>
	<li>Mysql Database</li>
	<li>Other python libraries like Mysqldb etc</li>
</ul>
<h4>Usage:</h4>
<ul class="list-style-type:disc">
	<li>Install all the requirements as stated above</li>
	<li>change the paths and database table name,fields in the files index.py,search.py,save_data.py and 
	search_img.py</li>
	<li>Run the main.py script</li>
	<li>Select the method from dropdown provided</li>
	<li>Enter the path of CSV file for indexing in case of color histogram and folder path as required,
	it can be made dynamic as required,i have,however fixed the paths.</li>
	<li>finally enter one of the image in the dataset as query image(full name)</li>
	<li>click on search to find the similar images</li>
</ul>
