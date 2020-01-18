<!DOCTYPE html>
<html>
<body>

<h1>My first PHP page</h1>

<?php
include "GeoserverWrapper.php";$geoserver = new GeoserverWrapper('http://localhost:5555/geoserver',$admin, $geoserver);
public function createWorkspace($workspaceName)-->$geoserver->createWorkspace('delineation_34');
?>

</body>
</html> 