<?php
$account_name = $_POST["account_name"];
$password = $_POST["password"];

$conexion = mysql_connect("localhost:1234", "root","1234");
mysql_select_db("letournee",$conexion);

$sql = "SELECT name FROM user WHERE account_name = '$account_name' AND'$password'";
$comprobar = mysql_query($sql);

if(mysql_nu_rows($comprobar)>0){
    $name = mysql_result($comprobar,0);
    setcookie("letournne","$name",time()+ 3600);
    header("Location: inicio.php");
    
}else
    echo "Usuario no registrado";
?>