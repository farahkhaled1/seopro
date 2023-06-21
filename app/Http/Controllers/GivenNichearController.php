<?php

namespace App\Http\Controllers;
use Symfony\Component\Process\Process;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class GivenNichearController extends Controller
{

    public function store_niche_ar(Request $request)
    {
        $validatedData = $request->validate([
            'niche' => 'required|max:255',
        ]);

        $user_id = Auth::id(); // Get the current user's id

        DB::table('given_niche_ar')->insert([
            'uid' => $user_id, // Store the user id
            'niche' => $validatedData['niche'],
        ]);




        $request->session()->put('niche',$validatedData['niche']);
        if( self::runPythonScriptWithShell()){
            return redirect()->back();
        }
        // return redirect()->back()->with(["error"=>"Failed to process your request. Please try again later."]);
        return redirect()->back();
    }
    private static function runPythonScriptWithShell()
    {
        $pythonScriptPath = 'tf_idf_ar.py';
        $absolute_path = (("../python/Arabic/".$pythonScriptPath));
        $output = shell_exec("cd ".public_path()."&& python \"".$absolute_path."\" ERROR 2>&1");
        if(trim($output) == "success")
            return true;
        return false;
    }   
}

?>







