<?php
    exec("python3 m1.py");
    exec("python3 cleaner.py");
    header("Location:./index.php?id=3");
?>
