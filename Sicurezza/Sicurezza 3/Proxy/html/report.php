<?php
// Simulazione carico di lavoro (sleep)
usleep(1500000+rand(-1500000/5, 1500000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: report.php</title></head>
<body>
    <h1>Modulo Dinamico: report.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 1500 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
