import praw
import pandas as pd

# --- 1) Reddit API Credentials ---
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent=''
)

# --- 2) Revised List of Reddit Post URLs ---

    
urls = [
    "https://www.reddit.com/r/OpenAI/comments/1jp4axw/why_are_my_sora_images_low_resolution/",
    "https://www.reddit.com/r/OpenAI/comments/1jr1xai/anthropic_research_paper_reasoning_models_dont/",
    "https://www.reddit.com/r/OpenAI/comments/1jqnyxt/not_sure_if_using_ai_for_fusion_360_design_is_a/",
    "https://www.reddit.com/gallery/1jscwas",
    "https://www.reddit.com/r/OpenAI/comments/1jqaszf/anyone_else_getting_stuck_on_creating_image_on_a/",
    "https://www.reddit.com/r/OpenAI/comments/1jq72rh/emotional_intelligence_and_theory_of_mind_for/",
    "https://www.reddit.com/r/OpenAI/comments/1jrj41u/virtual_scroll_for_browser_version/",
    "https://www.reddit.com/r/OpenAI/comments/1jptv5c/petition_to_nerf_the_image_generation_content/",
    "https://www.reddit.com/r/OpenAI/comments/1jqrh55/all_professionals_might_soon_be_parttime_junior/",
    "https://www.reddit.com/r/OpenAI/comments/1jqu1ta/why_i_love_ai_as_a_poor_gig_economy_artist_who_is/",
    "https://www.reddit.com/r/OpenAI/comments/1jsb1jf/new_llama_model/",
    "https://www.reddit.com/r/OpenAI/comments/1jqnxgy/new_jobs_created_by_ai_that_arent_prompt/",
    "https://www.reddit.com/r/OpenAI/comments/1jpqssy/its_down_yes/",
    "https://www.reddit.com/r/OpenAI/comments/1jqitfb/give_a_pin_feature_where_users_can_pin_their/",
    "https://www.reddit.com/r/OpenAI/comments/1jpiqfm/how_can_i_use_gpt_in_my_work/",
    "https://www.reddit.com/r/OpenAI/comments/1js2pug/extract_handwriting_from_pdfs/",
    "https://www.reddit.com/gallery/1joyw3l",
    "https://www.reddit.com/gallery/1jrdkc4",
    "https://www.reddit.com/r/OpenAI/comments/1jqfdnw/imagine_gaming_for_years_only_to_realize_every/",
    "https://www.reddit.com/r/OpenAI/comments/1jqdn2b/content_policy_roulette/",
    "https://www.reddit.com/r/OpenAI/comments/1jqtfym/besides_studio_ghibli_lets_see_your_images_in/",
    "https://www.reddit.com/r/OpenAI/comments/1jp1zsi/infographics_with_the_4o_image_generator/",
    "https://www.reddit.com/r/OpenAI/comments/1jrfgyn/o3_pro_coming_soon/",
    "https://www.reddit.com/r/OpenAI/comments/1jrjcff/is_the_new_image_generator_available_as_an_api_yet/",        
    "https://www.reddit.com/gallery/1jqwbas",
    "https://www.reddit.com/r/OpenAI/comments/1jqeghp/anyone_else_not_able_to_generate_younger_family/",
    "https://www.reddit.com/r/OpenAI/comments/1jpj6wv/the_new_image_tool_has_gotten_a_massive_nerf_it/",
    "https://www.reddit.com/r/OpenAI/comments/1jpw7ft/how_do_i_turn_off_improved_memory/",
    "https://www.reddit.com/r/OpenAI/comments/1jqnd0x/ai_all_in_one/",
    "https://www.reddit.com/r/OpenAI/comments/1jp2hnq/how_do_you_take_these_ghibli_or_star_wars/",
    "https://www.reddit.com/r/OpenAI/comments/1jp45z7/do_pro_users_face_cooldowns_too/",
    "https://www.reddit.com/r/OpenAI/comments/1jqrdhe/gpt_plus_user/",
    "https://www.reddit.com/r/OpenAI/comments/1jp3neh/two_questions_about_sora/",
    "https://www.reddit.com/r/OpenAI/comments/1jrsez7/is_this_a_plausible_solution_to_the_context/",
    "https://www.reddit.com/r/OpenAI/comments/1jr751j/azure_openai_embeddings_endpoint_gives_error/",
    "https://www.reddit.com/r/OpenAI/comments/1jqresi/what_happened_to_my_canvas_files/",
    "https://www.reddit.com/gallery/1jqflus",
    "https://www.reddit.com/gallery/1jppfpv",
    "https://www.reddit.com/r/OpenAI/comments/1jq469w/a_thought_experiment_on_ai_and_stolen_art/",
    "https://www.reddit.com/r/OpenAI/comments/1jqplbe/how_much_of_the_internet_is_indexed_by_openai_in/",
    "https://www.reddit.com/r/OpenAI/comments/1jpnkbf/openai_plans_to_release_openweight_language_model/",
    "https://www.reddit.com/r/OpenAI/comments/1jrsq1o/theres_strong_likelihood_that_the_quasar_alpha/",
    "https://www.reddit.com/r/OpenAI/comments/1jse2qr/new_image_generator_not_available_in_the_mac/",
    "https://www.reddit.com/r/OpenAI/comments/1jry707/has_anyone_been_asked_do_you_like_this_models/",
    "https://www.reddit.com/r/OpenAI/comments/1jrxtrc/issues_with_just_one_generation_at_a_time/",
    "https://www.reddit.com/gallery/1jq6ge1",
    "https://www.reddit.com/r/OpenAI/comments/1jsaduf/the_essential_role_of_logic_agents_in_enhancing/",
    "https://www.reddit.com/r/OpenAI/comments/1jq17qx/image_gen_v2_out/",
    "https://www.reddit.com/r/OpenAI/comments/1jp7eeo/deep_research_bugged_when_writing_sources/",
    "https://www.reddit.com/r/OpenAI/comments/1jptnmo/monday_gpt_randomly_appeared/",
    "https://www.reddit.com/r/OpenAI/comments/1jsc3rt/we_can_make_ghibli_style_but_what_about_jojo/",
    "https://www.reddit.com/r/OpenAI/comments/1jqf9i4/til_openai_prepaid_credits_expires/",
    "https://www.reddit.com/gallery/1jpby8b",
    "https://www.reddit.com/r/OpenAI/comments/1jpwspl/what_other_styles_have_yall_gotten_to_work_dragon/",
    "https://www.reddit.com/r/OpenAI/comments/1jrjwai/just_here_to_say_ive_been_having_fun_interacting/",
    "https://www.reddit.com/gallery/1jpxp6l",
    "https://www.reddit.com/r/OpenAI/comments/1jqr16w/what_is_the_daily_limit_for_image_generation_for/",
    "https://www.reddit.com/r/OpenAI/comments/1jpeszp/systematically_prompting_ais_to_become_more/",
    "https://www.reddit.com/r/OpenAI/comments/1jrungc/the_peak_of_content_filters_with_their_new_image/",
    "https://www.reddit.com/r/OpenAI/comments/1js49gj/reduced_gpt_45_orion_rate_limits/",
    "https://www.reddit.com/r/OpenAI/comments/1jqdazu/mckinsey_company_the_state_of_ai_2025/",
    "https://www.reddit.com/r/OpenAI/comments/1jr7bm8/webinar_today_an_ai_agent_that_joins_across/",
    "https://www.reddit.com/r/OpenAI/comments/1jsdfgh/any_library_to_pass_tools_automatically_to_gpts/",
    "https://www.reddit.com/r/OpenAI/comments/1js9ftc/ai_is_automating_our_jobs_but_values_need_to/",
    "https://www.reddit.com/r/OpenAI/comments/1jr92go/fresh_account_couldnt_make_api_calls_wont_give_a/",
    "https://www.reddit.com/r/OpenAI/comments/1jpqeqy/4o_is_getting_a_lot_better/",
    "https://www.reddit.com/gallery/1jqpdpe",
    "https://www.reddit.com/r/OpenAI/comments/1jpc2l2/is_ai_having_any_real_negative_impact_on_anyones/",
    "https://www.reddit.com/r/OpenAI/comments/1jrxgiw/plus_users_are_still_stuck_with_32k_context/",
    "https://www.reddit.com/r/OpenAI/comments/1js7dax/suggestion_desktop_app_for_linux/",
    "https://www.reddit.com/gallery/1jqc2so",
    "https://www.reddit.com/r/OpenAI/comments/1jsfa20/because_a_picture_is_worth_a_thousand_words/",
    "https://www.reddit.com/gallery/1jr348c",
    "https://www.reddit.com/r/OpenAI/comments/1jrt9l5/how_do_gemini_gems_compare_against_custom_gpts/",
    "https://www.reddit.com/r/OpenAI/comments/1jpid1h/question_for_researchers_using_ai/",
    "https://www.reddit.com/r/OpenAI/comments/1js723m/how_to_write_like_human/",
    "https://www.reddit.com/r/OpenAI/comments/1jr8bkr/i_would_prefer_a_literesearch_product_from_openai/",
    "https://www.reddit.com/r/OpenAI/comments/1jpznkx/testing_manus_on_automating_systematic_challenge/",
    "https://www.reddit.com/r/OpenAI/comments/1jqcopo/anyone_using_the_tts_api_keep_getting_quota_error/",
    "https://www.reddit.com/r/OpenAI/comments/1jse7wf/why_responses_api_use_more_tokens/",
    "https://www.reddit.com/r/OpenAI/comments/1jptapu/paid_customer_prompts_should_have_priority_over/",
    "https://www.reddit.com/gallery/1jp9spg",
    "https://www.reddit.com/gallery/1jr98yp",
    "https://www.reddit.com/r/OpenAI/comments/1jpa3nc/ai_will_make_privacy_the_new_luxury_item/",
    "https://www.reddit.com/gallery/1jrs2u9",
    "https://www.reddit.com/r/OpenAI/comments/1jqowv8/i_built_an_opensource_operator_that_can_use/",
]
# Remove duplicate URLs
unique_urls = list(set(urls))

# --- 3) Process each URL to fetch submission details and its comments ---
all_comments_data = []

for url in unique_urls:
    print(f"Processing URL: {url}")
    try:
        # Fetch the submission for the given URL
        submission = reddit.submission(url=url)
        # Load all comments by replacing "more" objects
        submission.comments.replace_more(limit=None)
        comments = submission.comments.list()
        
        # Additional submission-level metadata
        submission_metadata = {
            'submission_id': submission.id,
            'submission_title': submission.title,
            'submission_url': url,
            'submission_score': submission.score,
            'submission_upvote_ratio': submission.upvote_ratio,
            'submission_num_comments': submission.num_comments,
            'submission_subreddit': str(submission.subreddit),
            'submission_is_self': submission.is_self,
            'submission_over_18': submission.over_18
        }
        
        # Collect metadata for each comment and merge with submission metadata
        for comment in comments:
            comment_data = {
                'comment_id': comment.id,
                'parent_id': comment.parent_id,
                'comment_body': comment.body,
                'comment_score': comment.score,
                'comment_gilded': comment.gilded,
                'comment_controversiality': comment.controversiality,
                'comment_edited': comment.edited,
                'comment_created_utc': comment.created_utc,
                'comment_author': str(comment.author),
                'comment_permalink': comment.permalink
            }
            record = {**submission_metadata, **comment_data}
            all_comments_data.append(record)
    except Exception as e:
        print(f"Error processing URL {url}: {e}")

# --- 4) Convert the collected data into a pandas DataFrame ---
df = pd.DataFrame(all_comments_data)

# Convert Unix timestamps to a human-readable datetime if data exists
if not df.empty:
    df['comment_created_utc'] = pd.to_datetime(df['comment_created_utc'], unit='s')

# --- 5) Save the DataFrame to a CSV file ---
csv_filename = 'multiple_reddit_posts_comments5.csv'
df.to_csv(csv_filename, index=False)

print(f"\nExtracted {len(df)} comments from {len(unique_urls)} posts.")
print(f"Data has been saved to '{csv_filename}'")