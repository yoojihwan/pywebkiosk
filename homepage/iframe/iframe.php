<!DOCTYPE html>
<html>
<head>
     <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <link rel="stylesheet" type="text/css" href="./style.css">
 
  <link href="./bootstrap-3.3.4-dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <?php
    if(empty($_GET['id'])){
        echo file_get_contents("no.php");
    }
    else{
        echo file_get_contents($_GET['id'].".php");
    }
    ?>
    <button type="button" class="btn btn-outline-success" onclick="location.href='./iframe.php?id=3'"/>학식</button>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="./bootstrap-3.3.4-dist/js/bootstrap.min.js"></script>
</body>
</html>
