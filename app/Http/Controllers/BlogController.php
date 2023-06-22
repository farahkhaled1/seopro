<?php

namespace App\Http\Controllers;
use Symfony\Component\Process\Process;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;
use App\Models\Blog;

class BlogController extends Controller
{
    public function index($id = null)
    {
        if($id != null){
            $blog = Blog::findOrFail($id);
            return view('editor', ['blog'=>$blog]);
        }
        
        return view('editor');
    }

    public function editor(Request $request)
    {
        $validatedData = $request->validate([
            'blog' => 'required',
        ]);
        
        $user_id = Auth::id(); // Get the current user's id

        DB::table('blog')->insert([
            'uid' => $user_id, // Store the user id
            'blog' => $validatedData['blog'],
        ]);

        // Store the niche value in the user's session
        $request->session()->put('blog', $validatedData['blog']);

        // return redirect()->back()->with('success', 'Niche keyword added successfully.');
        return redirect()->back();
    }

    public function editBlog(Request $request){
        $validatedData = $request->validate([
            'blog' => 'required',
            'id'=> 'required|exists:blog,blogid'
        ]);
        
        $user_id = Auth::id(); // Get the current user's id
        $id = $request->id;
        $blog = Blog::findOrFail($id);
        $blog->blog = $request->blog;
        $blog->timestamps = false;
        $blog->save();

        // Store the niche value in the user's session
        $request->session()->put('blog', $validatedData['blog']);

        // return redirect()->back()->with('success', 'Niche keyword added successfully.');
        return redirect()->back();
    }

    public function showBlogs()
    {
        $blogs = Blog::all();

        return view('virtual-reality', ['blogs' => $blogs]);
    }
}


?>







