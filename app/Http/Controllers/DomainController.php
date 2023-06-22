<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Mail;
use App\Mail\MailNotify;
use Exception;

// use 
class DomainController extends Controller
{
    public function index(){
        return view('analyzer');
    }
    
 public function result(Request $request){

    $topic = $request->topic;

    $date = date("d/m/y");

$curl = curl_init();

curl_setopt_array($curl, [
	CURLOPT_URL => "https://domain-seo-analysis.p.rapidapi.com/domain-seo-analysis/?domain=$topic&country=us",
	CURLOPT_RETURNTRANSFER => true,
	CURLOPT_FOLLOWLOCATION => true,
	CURLOPT_ENCODING => "",
	CURLOPT_MAXREDIRS => 10,
	CURLOPT_TIMEOUT => 30,
	CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
	CURLOPT_CUSTOMREQUEST => "GET",
	CURLOPT_HTTPHEADER => [
		"X-RapidAPI-Host: domain-seo-analysis.p.rapidapi.com",
		"X-RapidAPI-Key: e1d4c245damsha7dc645641ffd43p142231jsn3330afedca88"
	],
]);
$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);



if ($err) {
    echo "cURL Error #:" . $err;
} else {
    // $response_data = json_decode($response, true);
    // var_dump($response_data); // print the response data structure

$response_data = json_decode($response, true);
$domain_rank = $response_data['data']['domain_rank'];
$domain_auth = $response_data['data']['domain_authority'];
$ctr_scope = $response_data['data']['ctr_scope'];
$seo_difficulty = $response_data['data']['seo_difficulty'];
$off_page_difficulty = $response_data['data']['off_page_difficulty'];
$on_page_difficulty = $response_data['data']['on_page_difficulty'];
$indexed_pages = $response_data['data']['indexed_pages'];
$page_authority = $response_data['data']['page_authority'];
$popularity_score = $response_data['data']['popularity_score'];
$traffic = $response_data['data']['traffic'];
$traffic_costs = $response_data['data']['traffic_costs'];
$organic_keywords = $response_data['data']['organic_keywords'];
$backlinks = $response_data['data']['backlinks'];
$equity = $response_data['data']['equity'];
$cpc = $response_data['data']['cpc'];
$search_volume = $response_data['data']['search_volume'];


$user_id = Auth::id(); // Get the current user's id

        DB::table('domain_analytics')->insert([
            'domain_url' => $topic,
            'uid' => $user_id, // Store the user id
            'domain_rank'=> $domain_rank,
            'domain_auth'=> $domain_auth,
            'ctr_scope' => $ctr_scope,
            'seo_difficulty'=> $seo_difficulty,
            'off_page_difficulty' => $off_page_difficulty,
            'on_page_difficulty' => $on_page_difficulty,
            'indexed_pages' => $indexed_pages,
            'page_authority' => $page_authority,
            'popularity_score' => $popularity_score,
            'traffic' => $traffic,
            'traffic_costs'=> $traffic_costs,
            'organic_keywords' => $organic_keywords,
            'backlinks' => $backlinks,
            'equity' => $equity,
            'cpc' => $cpc,
            'search_volume'=>$search_volume,
            'date' => $date



            
        ]);


$data = [
    'domain_rank' => $domain_rank,
    'domain_auth' => $domain_auth,
    'ctr_scope' => $ctr_scope,
    'seo_difficulty' => $seo_difficulty,
    'off_page_difficulty' => $off_page_difficulty,
    'on_page_difficulty' => $on_page_difficulty,
    'indexed_pages' => $indexed_pages,
    'page_authority' => $page_authority,
    'popularity_score' => $popularity_score,
    'traffic' => $traffic,
    'traffic_costs' => $traffic_costs,
    'organic_keywords' => $organic_keywords,
    'backlinks' => $backlinks,
    'equity' => $equity,
    'cpc' => $cpc,
    'search_volume' => $search_volume,
];

$this->Mailindex($request);


return view('analyzer', ['result' => $data]);
// return view('analyzer',['result'=> $domain_rank, $domain_auth, $ctr_scope , $seo_difficulty, $off_page_difficulty, $on_page_difficulty, $indexed_pages, $page_authority, $popularity_score,$traffic,$traffic_costs, $organic_keywords, $backlinks, $equity, $cpc, $search_volume]);

}

}
 public function Mailindex(Request $request)
    {
        // Get the user ID and the greatest ID number from the domain_analytics table
        $userId = $request->user()->id;
        $maxId = DB::table('domain_analytics')
            ->where('uid', $userId)
            ->max('id');

        // Fetch the data for the greatest ID number
        $domainAnalytics = DB::table('domain_analytics')
            ->where('id', $maxId)
            ->first();

        if ($domainAnalytics) {
            // Prepare the data for the email body
            $data = [
                'subject' => 'Your Analytics Stats',
                'body' => "Dear SEOPro user, here are your latest analytics stats:\n\n" .
                    "Domain URL: " . $domainAnalytics->domain_url . "\n" .
                    "Domain Rank: " . $domainAnalytics->domain_rank . "\n" .
                    "Domain Authority: " . $domainAnalytics->domain_auth . "\n" 
                    // Add other fields as needed
            ];

            try {
                // Send the email
                Mail::to($request->user()->email)->send(new MailNotify($data));
                return redirect('/analyzer');
            } catch (Exception $th) {
                return redirect('/analyzer')->with('error', 'Error');
            }
        } else {
            return redirect('/analyzer')->with('error', 'No analytics data found.');
        }
    }
    // public function processData(Request $request)
    // {
    //     // Call the first function
    //     $this->result($request);
    
    //     // Call the second function
    //     $this->Mailindex($request);
    
    
    //     // Return a response if needed
    //     }
}
