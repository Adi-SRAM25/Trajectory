import cv as Cv2
import matplotlib 


static void Process( string filename ) {
        Mat raw;

        raw = Cv2.ImRead( filename, ImreadModes.GrayScale );

        Mat threshold = new Mat();
        Cv2.Threshold( raw, threshold, 190, 255, ThresholdTypes.Otsu );

        Point[][] contours;
        HierarchyIndex[] hierarchyIndexes;

        Cv2.FindContours( threshold, out contours, out hierarchyIndexes, RetrievalModes.List, ContourApproximationModes.ApproxSimple );

        Mat rawColor = new Mat();
        Cv2.CvtColor( raw, rawColor, ColorConversionCodes.GRAY2RGB );

        if ( contours.Length != 0 ) {
            var contourIndex = 0;
            while ( contourIndex >= 0 ) {

                var area = Cv2.ContourArea( contours[ contourIndex ] );

                Debug.Print( $"{contourIndex} points: {contours[ contourIndex ].Length}, area: {area}" );

                //only look for features that have a given area
                if ( area < 1100000 && area > 400000.0 ) {
                //if ( area < 1100000 && area > 60000.0 ) {
                    Cv2.DrawContours( rawColor, contours, contourIndex, new Scalar( 255, 0, 0 ), 10, LineTypes.Link8, hierarchyIndexes, int.MaxValue );
                    Point centroid = Centroid( contours[ contourIndex ] );
                    Cv2.Circle( rawColor, centroid, 20, new Scalar( 0, 0, 255 ), 3 );

                    var radius = Math.Sqrt( area / Math.PI );
                    Cv2.Circle( rawColor, centroid, (int)radius, new Scalar( 0, 0, 255 ), thickness: 3 );

                }
                contourIndex = hierarchyIndexes[ contourIndex ].Next;
            }
        }
    }

    static Point Centroid ( Point[] knots ) {
        Point center = new Point();

        int sumofx = 0, sumofy = 0;

        for ( int i = 0; i < knots.Length; i++ ) {
            sumofx = sumofx + knots[ i ].X;
            sumofy = sumofy + knots[ i ].Y;
        }
        center.X = sumofx / knots.Length;
        center.Y = sumofy / knots.Length;

        return center;

    }
