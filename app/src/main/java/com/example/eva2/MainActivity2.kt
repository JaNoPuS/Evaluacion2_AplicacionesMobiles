package com.example.eva2

import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity

class MainActivity2 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Inicializar los elementos de la interfaz
        val etNombre = findViewById<EditText>(R.id.etNombre)
        val spOptions = findViewById<Spinner>(R.id.spOptions)
        val rgFrecuencia = findViewById<RadioGroup>(R.id.rgFrecuencia)
        val btnEnviar = findViewById<Button>(R.id.btnEnviar)

        // Configurar el Spinner con opciones
        val opciones = arrayOf("Horda", "Alianza", "Raza Aliada")
        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_item, opciones)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        spOptions.adapter = adapter

        // Configurar el evento de clic para el botón
        btnEnviar.setOnClickListener {
            val nombre = etNombre.text.toString()
            val comidaFavorita = spOptions.selectedItem.toString()
            val selectedRadioButtonId = rgFrecuencia.checkedRadioButtonId

            if (nombre.isEmpty() || selectedRadioButtonId == -1) {
                Toast.makeText(this, "Por favor, completa todos los campos.", Toast.LENGTH_SHORT).show()
            } else {
                val frecuencia = findViewById<RadioButton>(selectedRadioButtonId).text.toString()
                val resumen = "Nombre: $nombre\nFacción: $comidaFavorita\nFrecuencia de Juego: $frecuencia"

                // Crear y mostrar el AlertDialog
                val builder = AlertDialog.Builder(this)
                builder.setTitle("Resumen de la Encuesta")
                builder.setMessage(resumen)
                builder.setPositiveButton("OK") { dialog, _ ->
                    dialog.dismiss()
                }
                val dialog = builder.create()
                dialog.show()
            }
        }
    }
}