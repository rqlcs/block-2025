<?php
$musique = $_POST["music"];
$frequence = $_POST["frequency"];
$shell_cmd = escapeshellarg("python radio_web.py $musique $frequence");
exec($shell_cmd);
?>

<!DOCTYPE html>
<html lang="fr">
    <head>
        <title>&#127827 BerryRadio</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="retour">
                <a href="../index.php"><img src="assets/retour.png" width="20" height="20"></a>
        <div>
	<h1>&#127827<a class="image-clignote" href="https://github.com/rqlcs"> BerryR4DIO</a></h1>
	<p align="center"><img src="assets/onair.gif" width="300" height="70"></p>
	<br><br>
	<center>
		<div id="carre_rdiophp">
			<table>
				<thead>
					<tr>
						<th colspan="1">Radio Actived !</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td><br><br>Playing <?php echo "$musique"; ?></td>
					</tr>
					<tr>
						<td><br><br><br>On <?php echo "$frequence"; ?> MHz</td>
					</tr>
				</tbody>
			</table>
		</div>
		<div class="social_network">
			<div class="position_sn">
				<table>
					<tr>
						<td><img src="assets/twitter.png"</td>
						<td><a href="https://www.buymeacoffee.com/rqlcs.io"><img src="assets/buymeacoffee.png"</td></a>
					</tr>
				</table>
			</div>
		</div>	
        </center>
	<style>
		.retour{
			margin-top: 10px;
		}
		.position_sn{
			margin-left: -350px;
		}
		.position_sn img{
			opacity: 100%;
		}
		img{
			opacity: 70%;
		}

		table th{
			text-align: center;
			font-size: 18px;
			font-family: 'Retro Gaming';
		}
		table td{
			color: black;
			text-align: center;
			font-family: 'Retro Gaming';
			font-size: 15px;
		}
		#carre_rdiophp {
			width: 300px;
			height: 200px;
			background-color: #b2c7a7;
			border-radius: 10%;
		}
	</style>
    </body>
</html>

<!-- Made By RQLCS.-->
