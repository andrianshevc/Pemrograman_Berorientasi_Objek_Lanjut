<?php
require_once 'database.php';
require_once 'Anggota.php';
$db = new MySQLDatabase();
$anggota = new Anggota($db);
$id=0;
$kode_anggota=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_anggota'])){
            $kode_anggota = $_GET['kode_anggota'];
        }
        if($id>0){    
            $result = $anggota->get_by_id($id);
        }elseif($kode_anggota>0){
            $result = $anggota->get_by_kode_anggota($kode_anggota);
        } else {
            $result = $anggota->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new anggota
        $anggota->kode_anggota = $_POST['kode_anggota'];
        $anggota->nama_anggota = $_POST['nama_anggota'];
        $anggota->jk_anggota = $_POST['jk_anggota'];
        $anggota->prodi_anggota = $_POST['prodi_anggota'];
        $anggota->alamat_anggota = $_POST['alamat_anggota'];
       
        $anggota->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Anggota created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Anggota not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_anggota'])){
            $kode_anggota = $_GET['kode_anggota'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $anggota->kode_anggota = $_PUT['kode_anggota'];
        $anggota->nama_anggota = $_PUT['nama_anggota'];
        $anggota->jk_anggota = $_PUT['jk_anggota'];
        $anggota->prodi_anggota = $_PUT['prodi_anggota'];
        $anggota->alamat_anggota = $_PUT['alamat_anggota'];
        if($id>0){    
            $anggota->update($id);
        }elseif($kode_anggota<>""){
            $anggota->update_by_kode_anggota($kode_anggota);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Anggota updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Anggota update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_anggota'])){
            $kode_anggota = $_GET['kode_anggota'];
        }
        if($id>0){    
            $anggota->delete($id);
        }elseif($kode_anggota>0){
            $anggota->delete_by_kode_anggota($kode_anggota);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Anggota deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Anggota delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>