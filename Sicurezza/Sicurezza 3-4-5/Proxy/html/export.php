<?php
// Simulazione carico di lavoro (sleep)
usleep(2500000+rand(-2500000/5, 2500000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: export.php</title></head>
<body>
    <h1>Modulo Dinamico: export.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 2500 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
