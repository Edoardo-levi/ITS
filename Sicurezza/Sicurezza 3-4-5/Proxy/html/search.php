<?php
// Simulazione carico di lavoro (sleep)
usleep(800000+rand(-800000/5, 800000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: search.php</title></head>
<body>
    <h1>Modulo Dinamico: search.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 800 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
