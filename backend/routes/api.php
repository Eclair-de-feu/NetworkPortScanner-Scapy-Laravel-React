<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ScanController;

Route::post('/scans', [ScanController::class, 'store']);
Route::get('/scans', [ScanController::class, 'index']);