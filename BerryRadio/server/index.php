<!DOCTYPE html>
<html lang="fr">
    <head>
        <title>&#127827 BerryRadio</title>
        <link rel="stylesheet" href="src/style.css">
    </head>
    <body>
        <h1>&#127827<a class="image-clignote" href="https://github.com/rqlcs"> BerryR4DIO</a></h1>
        <br><br><br><br>
        <center>
            <form action="src/radio.php" method="POST">
		<div id="carre_liste_music">
                    <table>
                        <thead>
                            <tr>
                                <th colspan="2" align="center">Song List</th>
                            </tr>
                        </thead>
                        <tbody>
				<?php foreach(array_slice(scandir("/opt/berryradio/msic/"),2) as $musiques): ?>
			        <tr>
				    <td><?php echo $musiques; ?></td>
				    <td><INPUT type="radio" id="music_choice" name="music" value=<?php echo $musiques ?>> &#10004</td>
			        </tr>
				<?php endforeach; ?>
                        </tbody>
                    </table>
		</div>
                <div id="carre_cursor_frequency">
                    <p id="frequency_paragraph">Frequency [ <font color="red">87.5</font> ; <font color="red">108.8</font> ]</p>
                    <input type="range" id="frequency_choice_slide" name="frequency" min="87.5" max="108.8" oninput="num.value = this.value"><p id="mhz_output"><font color="red"><output id="num">87.5</output></font> MHz</p>
                </div>
                <div id="carre_sending">
                    <p id="carre_sending_paragraph"> Let's Go !</p>
                    <div id="bouton-send">
			<input type="submit" type="button" id="sending_input" value="Send">
                        </form>
                    </div>
                    <div id="bouton-stop">
                        <form method="POST" action="src/stop.php">
                        <input type="submit" type="button" id="stop" value="Stop">
                        </form>
                    </div>
                </div>
		<div class="social_network">
			<table>
				<tr>
					<td><img src="src/assets/twitter.png"</td>
					<td><a href="https://www.buymeacoffee.com/rqlcs.io"><img src="src/assets/buymecoffee.png"</td></a>
				</tr>
			</table>
		</div>	
        </center>
    </body>
</html>

<!-- Made By RQLCS.-->
