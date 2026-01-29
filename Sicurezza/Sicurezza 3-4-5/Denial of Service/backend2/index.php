<?php
$start = microtime(true);
// Simuliamo un carico CPU: calcolo hash ripetuto
$hash = "start";
//sleep(1);
for($i = 0; $i < 100000; $i++) {
$hash = hash('sha256', $hash . $i);
}
$end = microtime(true);
$time = $end - $start;
echo "<h1>Benvenuto su Backend</h1>";
echo "<p>Pagina generata in " . round($time, 4) . " secondi.</p>";
echo "<p>IP Server: " . $_SERVER['SERVER_ADDR'] . "</p>";
?>