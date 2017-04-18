<?php
mysql_connect('localhost','root','1234') or die("Error al conectar " . mysql_error());
mysql_select_db('letournee') or die ("Error al seleccionar la Base de datos: " . mysql_error());

$account_name = $_POST['account_name'];
$pass = $_POST['password'];
  
 
$result = mysql_query("SELECT * from user where account_name ='" $account_name "'");
 
if($row = mysql_fetch_array($result)){
if($row['password'] == $pass){
session_start();
$_SESSION['account_name'] = $account_name;
header("Location: /templates/usuarios.html");
}else{
header(" Location: index.html");
exit();
}
}else{
header("Location: index.html");
exit();
}
?>