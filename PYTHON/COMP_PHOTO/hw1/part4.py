import sys
import os
import numpy as np
import cv2
from scipy.signal import convolve2d
from scipy.ndimage.filters import gaussian_filter
import math

import part0
import part1
import part2
import part3
import run

def sobel_filter_x():
  '''Return a 3x3 sobel filter in the x direction.
  '''
  return np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

def sobel_filter_y():
  '''Return a 3x3 sobel filter in the y direction.
  '''
  return np.array([[-1,-2,-1],
                   [ 0, 0, 0],
                   [ 1, 2, 1]])

def transform_xy_theta(dx, dy):
  '''Transform from xy gradients to edge direction.
  
  Input:

  dx, dy - the gradient images generated by applying sobel filters to an
  image. They both have shape (rows, cols) and dtype float.

  Output:

  theta - a numpy array of shape (rows, cols) and dtype float.
  
  Each location theta[i,j] should contain the inverse tangent of dy[i,j]/dx[i,j]
  , in the range of [-pi/2, pi/2] radiants.

  Hint: you may find the np.arctan function useful here.
  '''
  
  # To avoid dividing by zero, set dy to a small value in locations where it
  # is zero.
  dx[dx == 0] = 0.001

  theta = None
  
  # Insert your code here -------------------------------------------------------

  #------------------------------------------------------------------------------
  
  return theta

def transform_xy_mag(dx, dy):
  '''Transform from xy gradients to edge direction.
  
  Input:

  dx, dy - the gradient images generated by applying sobel filters to an
  image. They both have shape (rows, cols) and dtype float.

  Output:

  mag - a numpy array of shape (rows, cols) and dtype float.
  
  Each location mag[i,j] should contain the magnitude of the gradient, which
  is sqrt(dx[i,j]^2 + dy[i,j]^2)

  Hint: you may find the np.sqrt and np.square funcitons useful here.
  '''
  
  mag = None
  
  # Insert your code here -------------------------------------------------------

  #------------------------------------------------------------------------------
  
  return mag

def get_color(theta, mag):
  '''Return the color for a given edge theta and magnitude.

  Given the local edge orientation and magnitude, return the corresponding
  color. The intensity of the color is given by the magnitude (stronger edges
  are brighter)
  '''

  boundaries = np.array([0.375, 0.125, -0.125, -0.375]) * math.pi

  # crop the magnitude to 0, 255 range.
  if mag < 0:
    mag = 0

  if mag > 255:
    mag = 255

  # (vertical) | yellow
  if theta > boundaries[0] or theta < boundaries[3] :
    return (0, mag, mag)
  
  # \ green
  if theta >= boundaries[3] and theta < boundaries[2] :
    return (0, mag, 0)

  # -- blue
  if theta >= boundaries[2] and theta < boundaries[1] :
    return (mag, 0, 0)
  
  # / red
  if theta >= boundaries[1] and theta < boundaries[0] :
    return (0, 0, mag)

def run_edges(image):
  ''' This function finds and colors all edges in the given image.
  '''

  # Convert image to gray
  if len(image.shape) > 2:
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  else:
    grayimage = image

  # blur so the gradient operation is less noisy.
  # uses a gaussian filter with sigma = 2
  grayimage = gaussian_filter(grayimage, 2).astype(float)
  
  # Filter with x and y sobel filters
  dx = convolve2d(grayimage, sobel_filter_x())
  dy = convolve2d(grayimage, sobel_filter_y())
  
  # Convert to orientation and magnitude images
  theta = transform_xy_theta(dx, dy)
  mag = transform_xy_mag(dx, dy)

  outimg = np.zeros((image.shape[0], image.shape[1], 3), dtype = np.uint8)

  # Fill with corresponding color.
  for r in range(outimg.shape[0]):
    for c in range(outimg.shape[1]):
      outimg[r,c,:] = get_color(theta[r,c], mag[r,c])

  return outimg

def test():
  '''This script will perform a unit test on your function, and provide useful
  output.
  '''

  dxs = []
  dys = []
  thetas = []
  mags = []

  y = np.array([[ 0, 1],
                [-1, 0]], dtype = float)
  dys.append(y)

  x = np.array([[ 1, 0],
                [ 0,-1]], dtype = float)
  dxs.append(x)
  
  theta = np.array([[ 0.  ,  math.pi/2],
                    [-math.pi/2,  0.  ]], dtype = float)
  thetas.append(theta)

  mag = np.array([[ 1, 1],
                  [ 1, 1]], dtype = float)
  mags.append(mag)

  y = np.array([[ 0, 0, 0],
                [ 1, 1, 1],
                [-1,-1,-1]], dtype = float)
  dys.append(y)

  x = np.array([[ 0, 1,-1],
                [ 0, 1,-1],
                [ 0, 1,-1]], dtype = float)
  dxs.append(x)
  
  theta = np.array([[         0,          0,          0],
                    [ math.pi/2,  math.pi/4, -math.pi/4],
                    [-math.pi/2, -math.pi/4,  math.pi/4]], dtype = float)
  thetas.append(theta)

  mag= np.array([[ 0,     1,     1],
                 [ 1, 1.414, 1.414],
                 [ 1, 1.414, 1.414]], dtype = float)
  mags.append(mag)

  for dx, dy, theta, mag in zip(dxs, dys, thetas, mags):
    if __name__ == "__main__":
      print "dx:\n{}\n, dy:\n{}\n".format(dx, dy)

    usr_theta = transform_xy_theta(dx, dy)
    usr_mag = transform_xy_mag(dx, dy)

    for usr_out, true_out, name in zip((usr_theta, usr_mag), (theta, mag), ('theta', 'mag')):
      if not type(usr_out) == type(true_out):
        if __name__ == "__main__":
          print "Error- {} has type {}. Expected type is {}.".format(
              name, type(usr_out), type(true_out))
        return False

      if not usr_out.shape == true_out.shape:
        if __name__ == "__main__":
          print "Error- {} has shape {}. Expected shape is {}.".format(
              name, usr_out.shape, true_out.shape)
        return False

      if not usr_out.dtype == true_out.dtype:
        if __name__ == "__main__":
          print "Error- {} has dtype {}. Expected dtype is {}.".format(
              name, usr_out.dtype, true_out.dtype)
        return False

      if not np.all(np.abs(usr_out - true_out) < .05):
        if __name__ == "__main__":
          print "Error- {} has value:\n{}\nExpected value:\n{}".format(
              name, usr_out, true_out)
        return False

      if __name__ == "__main__":
        print "{} passed.".format(name)

  if __name__ == "__main__":
    print "Success."
  return True

if __name__ == "__main__":
  print "Performing unit tests. Your functions will be accepted if your result is\
within 0.05 of the correct output."
  np.set_printoptions(precision=3)
  if not test():
    print "Unit test failed. Halting"
    sys.exit() 

  sourcefolder = os.path.abspath(os.path.join(os.curdir, 'images', 'source'))
  outfolder = os.path.abspath(os.path.join(os.curdir, 'images', 'filtered'))

  print 'Searching for images in {} folder'.format(sourcefolder)

  # Extensions recognized by opencv
  exts = ['.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpg', 
    '.jpe', '.jp2', '.tiff', '.tif', '.png']

  # For every image in the source directory
  for dirname, dirnames, filenames in os.walk(sourcefolder):
    for filename in filenames:
      name, ext = os.path.splitext(filename)
      if ext in exts:
        print "Reading image {}.".format(filename)
        img = cv2.imread(os.path.join(dirname, filename))

        print "Applying edges."
        outimg = run_edges(img)
        outpath = os.path.join(outfolder, name + 'edges' + ext)

        print "Writing image {}.".format(outpath)
        cv2.imwrite(outpath, outimg)
