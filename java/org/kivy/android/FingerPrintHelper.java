package org.kivy.android;

import android.app.Activity;
import android.content.Context;
import android.hardware.fingerprint.FingerprintManager;
import android.os.CancellationSignal;
import android.widget.Toast;

public class FingerprintHelper {
    public static void authenticate(final Activity activity) {
        FingerprintManager fingerprintManager = (FingerprintManager) activity.getSystemService(Context.FINGERPRINT_SERVICE);
        if (!fingerprintManager.isHardwareDetected()) {
            Toast.makeText(activity, "No fingerprint hardware detected.", Toast.LENGTH_SHORT).show();
            return;
        }
        if (!fingerprintManager.hasEnrolledFingerprints()) {
            Toast.makeText(activity, "No fingerprints enrolled.", Toast.LENGTH_SHORT).show();
            return;
        }
        CancellationSignal cancellationSignal = new CancellationSignal();
        fingerprintManager.authenticate(null, cancellationSignal, 0, new FingerprintManager.AuthenticationCallback() {
            @Override
            public void onAuthenticationSucceeded(FingerprintManager.AuthenticationResult authenticationResult) {
                
                Toast.makeText(activity, "Fingerprint authenticated!", Toast.LENGTH_SHORT).show();
                
                activity.getSharedPreferences("auth", Context.MODE_PRIVATE)
                        .edit().putBoolean("fingerprint_success", true).apply();
                // You can set a shared preference or send a broadcast here for Python to check
            }
            @Override
            public void onAuthenticationFailed() {
                Toast.makeText(activity, "Fingerprint authentication failed.", Toast.LENGTH_SHORT).show();
            }
        }, null);
    }
}