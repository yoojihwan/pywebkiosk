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
<body id="target">
  <div class="container">
 
    <header class="jumbotron text-center">
      <img src="https://avatar.maplestory.nexon.com/Character/KJKKCPOHLNLMEPCFJPPOEOLGHDPEKPKDPHBCFCDADDDFFPJMLGHICKJLLLKKEJGCGNNEOIFAFBDFHHABKLHJFIIPCACPCGIAHDJAJJHNGLLGHIAHGHBDDHIDGCEEMNNKCLNHDJANNOFKJANHNEJJLGCHMINNCIPAAPJKKKLMMIGILHAFBIFMOCAMHPOPFELPGIJODCHDBPHIEILHGLEPMAHKAFNKIPBHAMJOEKJLALNMLOOCNBLMPFBGMFLLOIGO.png" alt="주군의비숍"
                         class="img-circle" id="logo">
        <h1><a href="./index.php">메인 화면</a></h1>
    </header>
    <div class="row">
 
        <nav class="col-md-3">
          <ol class="nav nav-pills nav-stacked">
          <?php
            echo file_get_contents("list.txt");
          ?>
          </ ol>
        </nav>
        <div class="col-md-9">
 
          <article>
          <?php
          if(empty($_GET['id']) === false ) {
              if($_GET['id']==3){
                  echo file_get_contents("menu_clean.txt");
              }
              else{
                  echo file_get_contents($_GET['id'].".txt");
              }
          }
          ?>
          </article>
          <hr>
          <div id="control">
            <div class="btn-group" role="group" aria-label="...">
              <input type="button" value="white" onclick="document.getElementById('target').className='white'" class="btn btn-default  btn-lg"/>
              <input type="button" value="black" onclick="document.getElementById('target').className='black'" class="btn btn-default btn-lg"/>
            </div>
        </div>
 
 
 
 
  </div>
 
 
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="./bootstrap-3.3.4-dist/js/bootstrap.min.js"></script>
</body>
</html>
