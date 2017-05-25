# Pico-CTF 2014: Droid App

**Category:** Forensics
**Points:** 80
**Total Solves:** Not Available
## Problem Description:

[//]: # (> This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found [here](format.c\).)
> An Android application was released for the toaster bots, but it seems like this one is some sort of debug version. Can you discover the presence of any debug information being stored, so we can plug this?
You can download the apk [here](https://picoctf.com/problem-static/forensics/DroidApp/ToasterBot.apk).

## Write-up
[//]: # (> Your write up goes here.)
> We are given an app apk and we need some information about source, so first we need to decompile the app for that we can use any online decompiler like [http://www.decompileandroid.com/](http://www.decompileandroid.com/). 
> After decompling, download the source of app in zip format and unzip it.
> To get info about debug information we can do grep on whole source of app for Debug in src directory of app.
```bash
grep -r "Debug" 
grep -r "Debug" .
./smali/android/support/v4/app/Fragment.smali:    invoke-static {p0, v0}, Landroid/support/v4/util/DebugUtils;->buildShortClassTag(Ljava/lang/Object;Ljava/lang/StringBuilder;)V
./smali/android/support/v4/app/FragmentManager.smali:.method public static enableDebugLogging(Z)V
./smali/android/support/v4/app/FragmentManagerImpl.smali:    invoke-static {v1, v0}, Landroid/support/v4/util/DebugUtils;->buildShortClassTag(Ljava/lang/Object;Ljava/lang/StringBuilder;)V
./smali/android/support/v4/app/FragmentManagerImpl.smali:    invoke-static {v1, v0}, Landroid/support/v4/util/DebugUtils;->buildShortClassTag(Ljava/lang/Object;Ljava/lang/StringBuilder;)V
./smali/android/support/v4/app/LoaderManager.smali:.method public static enableDebugLogging(Z)V
./smali/android/support/v4/app/LoaderManagerImpl$LoaderInfo.smali:    invoke-static {v1, v0}, Landroid/support/v4/util/DebugUtils;->buildShortClassTag(Ljava/lang/Object;Ljava/lang/StringBuilder;)V
./smali/android/support/v4/app/LoaderManagerImpl.smali:    invoke-static {v1, v0}, Landroid/support/v4/util/DebugUtils;->buildShortClassTag(Ljava/lang/Object;Ljava/lang/StringBuilder;)V
./smali/android/support/v4/content/Loader.smali:    invoke-static {p1, v0}, Landroid/support/v4/util/DebugUtils;->buildShortClassTag(Ljava/lang/Object;Ljava/lang/StringBuilder;)V
./smali/android/support/v4/content/Loader.smali:    invoke-static {p0, v0}, Landroid/support/v4/util/DebugUtils;->buildShortClassTag(Ljava/lang/Object;Ljava/lang/StringBuilder;)V
./smali/android/support/v4/util/DebugUtils.smali:.class public Landroid/support/v4/util/DebugUtils;
./smali/android/support/v4/util/DebugUtils.smali:.source "DebugUtils.java"
./smali/android/support/v7/internal/view/menu/ActionMenuView$LayoutParams.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/view/menu/ActionMenuView$LayoutParams.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/view/menu/ActionMenuView$LayoutParams.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/view/menu/ActionMenuView$LayoutParams.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/view/menu/ActionMenuView$LayoutParams.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/view/menu/MenuItemImpl.smali:    .annotation runtime Landroid/view/ViewDebug$CapturedViewProperty;
./smali/android/support/v7/internal/view/menu/MenuItemImpl.smali:    .annotation runtime Landroid/view/ViewDebug$CapturedViewProperty;
./smali/android/support/v7/internal/widget/AdapterViewICS.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/widget/AdapterViewICS.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/widget/AdapterViewICS.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/widget/AdapterViewICS.smali:    .annotation runtime Landroid/view/ViewDebug$ExportedProperty;
./smali/android/support/v7/internal/widget/AdapterViewICS.smali:    .annotation runtime Landroid/view/ViewDebug$CapturedViewProperty;
./smali/android/support/v7/internal/widget/AdapterViewICS.smali:    .annotation runtime Landroid/view/ViewDebug$CapturedViewProperty;
./smali/android/support/v7/internal/widget/AdapterViewICS.smali:    .annotation runtime Landroid/view/ViewDebug$CapturedViewProperty;
./smali/picoapp453/picoctf/com/picoapp/ToasterActivity.smali:    const-string v0, "Debug tag"
Binary file ./source.zip matches
./src/android/support/v4/app/Fragment.java:import android.support.v4.util.DebugUtils;
./src/android/support/v4/app/Fragment.java:        DebugUtils.buildShortClassTag(this, stringbuilder);
./src/android/support/v4/app/FragmentManager.java:    public static void enableDebugLogging(boolean flag)
./src/android/support/v4/app/FragmentManagerImpl.java:import android.support.v4.util.DebugUtils;
./src/android/support/v4/app/FragmentManagerImpl.java:            DebugUtils.buildShortClassTag(mParent, stringbuilder);
./src/android/support/v4/app/FragmentManagerImpl.java:            DebugUtils.buildShortClassTag(mActivity, stringbuilder);
./src/android/support/v4/app/LoaderManager.java:    public static void enableDebugLogging(boolean flag)
./src/android/support/v4/app/LoaderManagerImpl$LoaderInfo.java:import android.support.v4.util.DebugUtils;
./src/android/support/v4/app/LoaderManagerImpl$LoaderInfo.java:        DebugUtils.buildShortClassTag(mLoader, stringbuilder);
./src/android/support/v4/app/LoaderManagerImpl.java:import android.support.v4.util.DebugUtils;
./src/android/support/v4/app/LoaderManagerImpl.java:            DebugUtils.buildShortClassTag(mLoader, stringbuilder);
./src/android/support/v4/app/LoaderManagerImpl.java:        DebugUtils.buildShortClassTag(mActivity, stringbuilder);
./src/android/support/v4/content/Loader.java:import android.support.v4.util.DebugUtils;
./src/android/support/v4/content/Loader.java:        DebugUtils.buildShortClassTag(obj, stringbuilder);
./src/android/support/v4/content/Loader.java:        DebugUtils.buildShortClassTag(this, stringbuilder);
./src/android/support/v4/util/DebugUtils.java:public class DebugUtils
./src/android/support/v4/util/DebugUtils.java:    public DebugUtils()
./src/picoapp453/picoctf/com/picoapp/ToasterActivity.java:        Log.d("Debug tag", mystery);
```
> Looking at all the files listed in this get flag in file `./src/picoapp453/picoctf/com/picoapp/ToasterActivity.java`
```java
    public ToasterActivity()
    {
        mystery = new String(new char[] {
            'f', 'l', 'a', 'g', ' ', 'i', 's', ':', ' ', 'w', 
            'h', 'a', 't', '_', 'd', 'o', 'e', 's', '_', 't', 
            'h', 'e', '_', 'l', 'o', 'g', 'c', 'a', 't', '_', 
            's', 'a', 'y'
        });
    }
```
> Flag is : **what does_the__logcat_say**

## Other write-ups and resources

* None
