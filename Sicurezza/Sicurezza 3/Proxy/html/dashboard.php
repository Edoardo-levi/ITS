<?php
// Simulazione carico di lavoro (sleep)
usleep(500000+rand(-500000/5, 500000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: dashboard.php</title></head>
<body>
    <h1>Modulo Dinamico: dashboard.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 500 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
