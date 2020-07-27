# Camera calibration

The code in `calibration.py` can be used to complete collaboartion. Going through the script is fairly easy, and will be self-explanatory to understand.

However, to save time, here is a basic run-down of how to use it.

Run the script using:

```
python calibration.py
```

This will bring up the camera, with outlines to the chess board if you are using it.

When the camera has detected the chessboard, press `a` to capture the points for calibration.

You should capture at least 20 frames.


# Anglular displacement of objects in frame

The calibration data is useful in removing distortions in the camera image. Once the distortions are removed, we can calculate angular displacements by figuring out an extra parameter: the angular vision of the camera. Once we have that, we can use the ratio to determine the angle.

This is not an accurate measurement as it does require the distance, but we will see how we can mitigate these issues.
