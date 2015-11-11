<?php
// Connect to MySQL
$connection = mysqli_connect('127.0.0.1','username','password','name_mysql_database',port);
// Check connection
if (mysqli_connect_errno())
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

// Fetch the data
$query = "
  SELECT *
  FROM TableName
  ORDER BY Time ASC";
$result = mysqli_query($connection, $query );

// All good?
if ( !$result ) {
  // Nope
  $message  = 'Invalid query: ' . $query . "\n";
  $message .= 'Whole query: ' . $query;
  die( $message );
}

// Print out rows
$data = array();
while ( $row = mysqli_fetch_assoc( $result ) ) {
  $data[] = $row;
}
echo json_encode( $data );

// Close the connection
mysqli_close($connection);
?>