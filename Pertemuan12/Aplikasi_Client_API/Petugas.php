<?php
//Simpanlah dengan nama file : Petugas.php
require_once 'database.php';
class Petugas 
{
    private $db;
    private $table = 'petugas';
    public $kode_petugas = "";
    public $nama_petugas = "";
    public $jabatan_petugas = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kode_petugas(int $kode_petugas)
    {
        $query = "SELECT * FROM $this->table WHERE kode_petugas = $kode_petugas";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_petugas`,`nama_petugas`,`jabatan_petugas`) VALUES ('$this->kode_petugas','$this->nama_petugas','$this->jabatan_petugas')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_petugas = '$this->kode_petugas', nama_petugas = '$this->nama_petugas', jabatan_petugas = '$this->jabatan_petugas' 
        WHERE id_petugas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_petugas($kode_petugas): int
    {
        $query = "UPDATE $this->table SET kode_petugas = '$this->kode_petugas', nama_petugas = '$this->nama_petugas', jabatan_petugas = '$this->jabatan_petugas' 
        WHERE kode_petugas = $kode_petugas";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_petugas = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_petugas($kode_petugas): int
    {
        $query = "DELETE FROM $this->table WHERE kode_petugas = $kode_petugas";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>