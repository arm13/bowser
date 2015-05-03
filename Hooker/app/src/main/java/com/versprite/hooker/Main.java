package com.versprite.hooker;

import java.lang.reflect.Method;

import android.content.ComponentName;
import android.content.Intent;
import android.util.Log;
import com.saurik.substrate.*;


public class Main {

    private static String className = "android.content.Intent";

    static void initialize() {


        MS.hookClassLoad(className, new MS.ClassLoadHook() {
            @SuppressWarnings({ "unchecked", "rawtypes" })
            public void classLoaded(Class<?> _class) {
                Log.d("Hooker", "Class Loaded!");
                Method method;
                final String methodName = "parseUri";
                try{
                    method = _class.getMethod(methodName, String.class, Integer.TYPE);
                } catch (NoSuchMethodException e){
                    method = null;
                }

                if(method != null);
                    Log.d("Hooker", "Method Hooked!");

                MS.hookMethod(_class, method, new MS.MethodAlteration<Object, Intent>(){
                    public Intent invoked(Object _class, Object... args)
                        throws Throwable {
                        String arg1 = (String)args[0];
                        Log.d("Hooker", arg1);
                        Intent intent = invoke(_class, args);
                        String action = intent.getAction();
                        Log.d("Hooker", action);
                        return invoke(_class, args);
                    }
                });
            }
        });
    }
}