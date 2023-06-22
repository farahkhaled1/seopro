<?php


namespace App\Http\Controllers;

use Illuminate\Support\Facades\Mail;
use Illuminate\Support\Facades\DB;
use App\Mail\MailNotify;
use Exception;
use Illuminate\Http\Request;

class MailController extends Controller
{
    // public function Mailindex(Request $request)
    // {
    //     // Get the user ID and the greatest ID number from the domain_analytics table
    //     $userId = $request->user()->id;
    //     $maxId = DB::table('domain_analytics')
    //         ->where('uid', $userId)
    //         ->max('id');

    //     // Fetch the data for the greatest ID number
    //     $domainAnalytics = DB::table('domain_analytics')
    //         ->where('id', $maxId)
    //         ->first();

    //     if ($domainAnalytics) {
    //         // Prepare the data for the email body
    //         $data = [
    //             'subject' => 'Your Analytics Stats',
    //             'body' => "Dear SEOPro user, here are your latest analytics stats:\n\n" .
    //                 "Domain URL: " . $domainAnalytics->domain_url . "\n" .
    //                 "Domain Rank: " . $domainAnalytics->domain_rank . "\n" .
    //                 "Domain Authority: " . $domainAnalytics->domain_auth . "\n" 
    //                 // Add other fields as needed
    //         ];

    //         try {
    //             // Send the email
    //             Mail::to($request->user()->email)->send(new MailNotify($data));
    //             return redirect('/analyzer');
    //         } catch (Exception $th) {
    //             return redirect('/analyzer')->with('error', 'Error');
    //         }
    //     } else {
    //         return redirect('/analyzer')->with('error', 'No analytics data found.');
    //     }
    // }
}



// namespace App\Http\Controllers;
// use Illuminate\Support\Facades\Mail;
// use Illuminate\Support\Facades\DB;
// use App\Mail\MailNotify;
// use Exception;
// use Illuminate\Http\Request;

// class MailController extends Controller
// {
    
//     public function Mailindex(Request $request){
//         $data = [
//             'subject' => 'Your Analytics Stats ',
//             'body' =>"Dear SEOPro user"


//         ];
        
    
//         try {

//             Mail::to('farahkhalid556@gmail.com')->send(new MailNotify($data));
//             return redirect('/analyzer');
//         } 
        
//         catch (Exception $th) 
//         {
//             return redirect('/analyzer')->with('error', 'Error');
//         }
//     }
// }




// namespace App\Http\Controllers;
// use Illuminate\Support\Facades\Mail;
// use Illuminate\Support\Facades\DB;
// use App\Mail\MailNotify;
// use Exception;
// use Illuminate\Http\Request;

// class MailController extends Controller
// {
    
//     public function Mailindex(Request $request){
//         $data = [
//             'subject' => 'Your Analytics Stats ',
//             // 'body' => 'This is to confirm that the event of TEDxMIUFIHRI will be held on Friday  3/2 at Gusour Cultural Center Venue. Doors will open at 3:30 PM .\n\nWe are looking forward to having you as a participant in the FIHRI experience. \n\nFor more info check our Facebook page  "<br /> https://www.facebook.com/TEDxMIU?mibextid=LQQJ4d Regards,TEDxMIU'
//             // 'body' =>"Dear ".$request->input("name")." SEOPro ".$request->input('button_number')
//             'body' =>"Dear SEOPro user"


//         ];
        
    
//         try {
//             // Mail::to($request->input('email'))->send(new MailNotify($data));
//             // return redirect('/form')->with('success', 'Check Your Email Inbox!');

//             Mail::to('farahkhalid556@gmail.com')->send(new MailNotify($data));
//             return redirect('/analyzer');
//         } 
        
//         catch (Exception $th) 
//         {
//             return redirect('/analyzer')->with('error', 'Error');
//         }
//     }
// }