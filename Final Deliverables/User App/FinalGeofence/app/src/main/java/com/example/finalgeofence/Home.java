package com.example.finalgeofence;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;

public class Home extends AppCompatActivity {

    Button checkButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        checkButton = findViewById(R.id.checkButton);
        checkButton.setOnClickListener(view -> {
            startActivity(new Intent(this, MapsActivity.class));
        });
    }
}