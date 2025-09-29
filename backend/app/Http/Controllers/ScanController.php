<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Scan;

class ScanController extends Controller
{
    public function store(Request $request)
    {
        $data = $request->validate([
            'results' => 'required|array',
        ]);
        $scan = Scan::create(['results' => $data['results']]);
        return response()->json($scan, 201);
    }

    public function index()
    {
        return response()->json(Scan::latest()->first());
    }
}