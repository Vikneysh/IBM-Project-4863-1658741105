package com.example.finalgeofence;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    boolean valid;
    Button loginButton;
    EditText emailIDET;
    EditText passwordET;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        emailIDET = findViewById(R.id.emailID);
        passwordET = findViewById(R.id.userPassword);
        loginButton = findViewById(R.id.loginButton);
        loginButton.setOnClickListener(view -> {
            checkFields(emailIDET);
            checkFields(passwordET);
            if(emailIDET.getText().toString().equals("jebaswinston55@gmail.com") && passwordET.getText().toString().equals("Jebas123")) {
                Toast.makeText(this, "LoggedIn Successfully!", Toast.LENGTH_LONG).show();
                startActivity(new Intent(this, Home.class));
            } else {
                Toast.makeText(this, "Try again, your credentials are not valid!", Toast.LENGTH_LONG).show();
            }
        });
    }

    public boolean checkFields(EditText textField) {
        if(textField.getText().toString().isEmpty()) {
            valid = false;
            textField.setError("Enter a value!");
        } else {
            valid = true;
        }
        return valid;
    }
}