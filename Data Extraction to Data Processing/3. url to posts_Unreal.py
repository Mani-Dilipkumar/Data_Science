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
    "https://www.reddit.com/gallery/xgs8vw",
    "https://www.reddit.com/gallery/1jhbplh",
    "https://www.reddit.com/r/Games/comments/16tisnu/horizon_forbidden_west_complete_edition_coming_to/",
    "https://www.reddit.com/r/pcgaming/comments/mnogto/epic_games_lost_almost_181_million_273_million_on/",        
    "https://www.reddit.com/r/unrealengine/comments/12fqe8t/hows_my_idea_a_cloud_hosted_collaborative_unreal/",    
    "https://www.reddit.com/r/Vive/comments/5dlx8r/google_earth_vr_makes_a_strong_case_for_the/",
    "https://www.reddit.com/r/WutheringWaves/comments/1cy2xvj/small_little_tip_for_potato_pc_players_like_me/",    
    "https://www.reddit.com/r/unrealengine/comments/u252d0/every_time_i_close_unreal_editor_5_or_click_save/",     
    "https://www.reddit.com/gallery/pfbtpm",
    "https://www.reddit.com/r/gamesuggestions/comments/1brr04f/i_want_an_immersive_survivalexploration_game_with/",
    "https://www.reddit.com/r/unrealengine/comments/1942l1d/my_c_files_disappear_whenever_i_start_unreal/",        
    "https://www.reddit.com/gallery/1f8u565",
    "https://www.reddit.com/r/Amd/comments/kjzojd/psa_disabling_epic_games_launcher_lowered_my/",
    "https://www.reddit.com/r/gamedev/comments/16uj5b0/epic_games_the_maker_of_fortnite_and_unreal/",
    "https://www.reddit.com/r/VALORANT/comments/1fwj87z/new_agent_select_tease_unreal_engine_5_confirmed/",        
    "https://www.reddit.com/gallery/rdzy8d",
    "https://www.reddit.com/r/gamedev/comments/2xomh1/unreal_engine_4_now_available_without/",
    "https://www.reddit.com/gallery/x393wz",
    "https://www.reddit.com/r/FortniteCreative/comments/1hikr1m/new_project_cant_be_opened_unreal_editor/",        
    "https://www.reddit.com/r/unrealengine/comments/1fupmi8/i_just_release_a_realistic_snow_blowing_effect/",      
    "https://www.reddit.com/gallery/128gm09",
    "https://www.reddit.com/r/RocketLeague/comments/1fi2wkx/no_unreal_engine_5_news/",
    "https://www.reddit.com/r/tipofmyjoystick/comments/1cfxo91/pc1990sgraphic_adventure_with_very_cool/",
    "https://www.reddit.com/r/Games/comments/roc74y/prey_2017_is_free_on_epic_games_store_today/",
    "https://www.reddit.com/r/xcom2mods/comments/1fdli2d/need_help_with_unreal_editor/",
    "https://www.reddit.com/r/pcgaming/comments/b8vh7d/someone_hacked_into_my_epic_games_lost_thousands/",
    "https://www.reddit.com/r/tipofmyjoystick/comments/1cod5uv/android7_2014_1016_photorealistic_graphics_2d/",    
    "https://www.reddit.com/r/UnrealEnginePlugins/comments/1gkydbb/dev_blog_how_we_integrated_umg_into_the_unreal/",
    "https://www.reddit.com/gallery/1jp1nv2",
    "https://www.reddit.com/r/Youtubesubscribers/comments/1fxhqp1/uncharted_4_remastered_photorealistic_graphics/",
    "https://www.reddit.com/r/Sub4Sub/comments/1g5rtwr/silent_hill_2_remake_photorealistic_graphics/",
    "https://www.reddit.com/gallery/nntlc6",
    "https://www.reddit.com/r/UnrealEngine5/comments/1gkvxjb/problems_with_unreal_editor_54_rolling_back_files/",  
    "https://www.reddit.com/r/mvci/comments/1cgdrrx/a_custom_unreal_editor_for_mvci_has_just_been/",
    "https://www.reddit.com/r/ZenlessZoneZero/comments/1jmqlgy/epic_games_buying_overlay_not_opening_for_ingame/", 
    "https://www.reddit.com/r/DestinyTheGame/comments/528n8q/a_few_months_ago_i_took_a_class_on_unreal_engine/",   
    "https://www.reddit.com/r/Games/comments/1hqhnvv/sifu_is_available_for_free_on_the_epic_games/",
    "https://www.reddit.com/r/unrealengine/comments/1gbzyfk/unreal_marketplace_favorites/",
    "https://www.reddit.com/r/unrealengine/comments/1d0yi8b/most_unreal_engine_tutorials_on_youtube_use_bad/",     
    "https://www.reddit.com/r/Youtubesubscribers/comments/1g5ruqr/silent_hill_2_remake_photorealistic_graphics/",  
    "https://www.reddit.com/r/unrealengine/comments/1ggklt2/smooth_rotation_in_unreal_engine_vr/",
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/p34ne6/kotaku_reports_that_the_gta_trilogy_is_being/",
    "https://www.reddit.com/r/Games/comments/gnyfva/civilization_vi_is_free_on_epic_games/",
    "https://www.reddit.com/r/Sub4Sub/comments/1baj2q8/need_for_speed_underground_2_winter_mod/",
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/1ja6fw1/amazon_games_montreal_is_developing_an_aaa_moba/",
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/16cdhag/vgc_reports_switch_2_was_demoed_with_the_matrix/",
    "https://www.reddit.com/r/Steam/comments/1d82d0b/i_used_to_believe_that_the_epic_store_bad_was/",
    "https://www.reddit.com/gallery/1hmnkmy",
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/1fxu1r4/halo_moving_to_unreal_engine/",
    "https://www.reddit.com/r/unrealengine/comments/1efftgp/rendering_foliage_in_sequencer_that_wont_load_in/",    
    "https://www.reddit.com/r/skyrimmods/comments/1h6nq36/skyrim_ported_to_unreal_engine/",
    "https://www.reddit.com/r/tipofmyjoystick/comments/1joxhi2/pc20232025coopfps_amonguslike_game_with_unreal/",   
    "https://www.reddit.com/r/gameDevClassifieds/comments/1jb43lj/job_offer_were_looking_for_an_unreal_editor_5/", 
    "https://www.reddit.com/r/civ/comments/1idabq8/this_epic_games_store_datamine_corroborates_the/",
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/1io9a04/sonic_racing_crossworlds_seems_to_be_using_unreal/",
    "https://www.reddit.com/r/thesims/comments/l3tuiz/photorealistic_sims_are_so_creepy_id_rather_have/",
    "https://www.reddit.com/r/OculusQuest/comments/18vh3h5/uevr_is_released_univeral_unreal_engine_vr/",
    "https://www.reddit.com/gallery/1htpwnd",
    "https://www.reddit.com/r/UnrealEngine5/comments/1dr136w/unreal_engine_5_pc_needed_for_son_2000/",
    "https://www.reddit.com/r/FortniteCreative/comments/1hikl4p/unreal_editor_crashes_every_time_i_try_to_launch/",
    "https://www.reddit.com/r/VALORANT/comments/1ftuk53/valorant_switching_to_unreal_engine_5_teasing_new/",       
    "https://www.reddit.com/r/unrealengine/comments/1crkqi2/blenderstyle_transform_controls_for_unreal_editor/",   
    "https://www.reddit.com/r/IAmA/comments/rgw4d6/i_was_a_programmer_and_level_designer_for_the/",
    "https://www.reddit.com/r/EnterTheGungeon/comments/1jr8l29/how_would_you_fill_if_enter_the_gungeon_3_turned/", 
    "https://www.reddit.com/gallery/1duf8qf",
    "https://www.reddit.com/r/tipofmyjoystick/comments/1bf5y73/pcxboxps420222023_trailer_for_an_unreleased/",      
    "https://www.reddit.com/r/GhostsOfTabor/comments/1csu722/for_those_worried_about_the_dev_time_of_the/",        
    "https://www.reddit.com/r/pcgaming/comments/brgq8p/reddit_user_requested_all_the_personal_info_epic/",
    "https://www.reddit.com/gallery/1gvyk2o",
    "https://www.reddit.com/r/Superstonk/comments/11z1lux/ill_be_honest_i_wasnt_sure_if_the_nft_digital/",
    "https://www.reddit.com/r/oculus/comments/xa2qmk/universal_unreal_engine_vr_injector_time_to_get/",
    "https://www.reddit.com/r/unrealengine/comments/1gl59k9/free_items_on_unreal_marketplace/",
    "https://www.reddit.com/r/Sub4Sub/comments/1fxhq0f/uncharted_4_remastered_photorealistic_graphics/",
    "https://www.reddit.com/r/unrealengine/comments/1gky6ry/dev_blog_how_we_integrated_umg_into_the_unreal/",      
    "https://www.reddit.com/r/unrealengine/comments/1frk812/unreal_marketplace_is_shutting_down_when_fab/",        
    "https://www.reddit.com/r/VRGaming/comments/1d91n7b/been_playing_operation_harshdoorstwp_with_unreal/",        
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/1jk8hmq/rocksteadys_next_batman_game_to_use_unreal_engine/",
    "https://www.reddit.com/r/Deusex/comments/1ex3rwr/how_do_i_convert_the_dx_format_of_the_deus_ex/",
    "https://www.reddit.com/r/unrealengine/comments/1jhy38q/best_learning_resources_for_unreal_editor_tooling/",   
    "https://www.reddit.com/r/gtaonline/comments/1j39i61/cant_get_gta_v_enhanced_for_free_on_epic_games/",
    "https://www.reddit.com/r/gamedev/comments/20tnfm/unreal_engine_4_has_been_launched/",
    "https://www.reddit.com/r/FortNiteBR/comments/11t4g7o/unreal_editor_for_fortnite_uefn_creative_20/",
    "https://www.reddit.com/r/unrealengine/comments/1i3mst1/glitch_with_vertical_objects_on_unreal_engine_vr/",    
    "https://www.reddit.com/r/unrealengine/comments/1d02wi5/unreal_marketplace_ignoring_my_request_for_refund/",   
    "https://www.reddit.com/r/applehelp/comments/1fjlmq7/unreal_editor_crashes_on_mac/",
    "https://www.reddit.com/gallery/1hnekwc",
    "https://www.reddit.com/r/AutoHotkey/comments/1j9zsns/unreal_editor_only_activating_if_activated/",
    "https://www.reddit.com/gallery/1dy7dxc",
    "https://www.reddit.com/r/FortniteCreative/comments/1hb2grr/latest_3310_update_for_unreal_editor_fortnite/",   
    "https://www.reddit.com/r/unrealengine/comments/1fjjxs7/unreal_editor_crashes_on_mac_os/",
    "https://www.reddit.com/r/FortniteCreative/comments/1bjblhs/help_with_unreal_editor_im_stupid_most_likely/",   
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/1bnqbrh/sonic_heroes_remake_is_in_development_using_the/",
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/q1yyu3/grand_theft_auto_remastered_trilogy_confirmed_to/",
    "https://www.reddit.com/r/unrealengine/comments/1g4dvx9/unreal_marketplace/",
    "https://www.reddit.com/gallery/s0iug6",
    "https://www.reddit.com/r/FortNiteBR/comments/1ekqb0j/epic_games_deleted_items_from_my_account_for_no/",       
    "https://www.reddit.com/r/civ/comments/4iw5cc/the_game_was_only_announced_a_couple_of_hours_ago/",
    "https://www.reddit.com/gallery/1i86923",
    "https://www.reddit.com/gallery/1g8sx52",
    "https://www.reddit.com/gallery/l9z4zq",
    "https://www.reddit.com/r/unrealengine/comments/15xuowm/unreal_marketplace_search_engine_really_needs/",       
    "https://www.reddit.com/r/unrealengine/comments/1biqj8p/mouse_lags_when_i_click_on_drop_down_menus_only/",     
    "https://www.reddit.com/gallery/1bnpu5f",
    "https://www.reddit.com/r/FortniteCreative/comments/1bnfd0h/unreal_editor_not_launching/",
    "https://www.reddit.com/r/Games/comments/kf02e9/cities_skyline_is_the_first_free_game_today_on/",
    "https://www.reddit.com/gallery/1gti8l9",
    "https://www.reddit.com/r/u_dragonsbfinance/comments/rnbxkc/dragonsb_the_first_nft_metaverse_mmorpg_based_on/",
    "https://www.reddit.com/gallery/1fxua3j",
    "https://www.reddit.com/r/virtualreality/comments/1fy24zh/huge_weird_shadow_in_unreal_engine_vr_preview/",     
    "https://www.reddit.com/r/startrek/comments/4c5wk7/star_trek_tng_unreal_engine_4_project/",
    "https://www.reddit.com/gallery/1hamiyp",
    "https://www.reddit.com/r/unrealengine/comments/n1e033/apple_ios_update_145_broke_unreal_engine_ar/",
    "https://www.reddit.com/r/unrealengine/comments/1h924ym/unreal_engine_is_killing_the_industry/",
    "https://www.reddit.com/r/pcgaming/comments/am18zn/here_is_why_epic_games_launcher_is_better_than/",
    "https://www.reddit.com/r/SubredditDrama/comments/cdukbm/epic_games_donates_12m_to_blender_an_open_source/",   
    "https://www.reddit.com/r/FreeGameFindings/comments/1iu2bhh/epic_games_mobile_game_star_wars_knights_of_the/", 
    "https://www.reddit.com/r/edgegap/comments/1dl6g0t/add_game_server_hosting_directly_from_the_unreal/",
    "https://www.reddit.com/r/discgolf/comments/1fzzhb4/we_are_creating_a_disc_golf_game_using_unreal/",
    "https://www.reddit.com/r/unrealengine/comments/1ihmimn/used_to_spend_hours_on_unreal_marketplace_cant_do/",   
    "https://www.reddit.com/r/virtualreality/comments/yk2vwu/does_photorealism_matter_in_a_vr_experience_name/",   
    "https://www.reddit.com/r/unrealengine/comments/1g9b1i5/unreal_marketplace_wishlist_fab/",
    "https://www.reddit.com/r/unrealengine/comments/10coonl/the_review_system_is_being_actively_gamed_on_the/",    
    "https://www.reddit.com/r/gaming/comments/1aldz7e/disney_invests_15b_in_epic_games/",
    "https://www.reddit.com/gallery/yzxv3l",
    "https://www.reddit.com/r/aximmetry/comments/1duhpyr/ue5_marketplace_not_compatible_with_aximmetry/",
    "https://www.reddit.com/r/Starfield/comments/1g18qlg/i_talked_to_skyrim_designer_bruce_nesmith_about/",        
    "https://www.reddit.com/gallery/1d5tsxl",
    "https://www.reddit.com/r/unrealengine/comments/1aemfwx/unreal_engine_ar_development_with_hololens_2_in/",     
    "https://www.reddit.com/r/gaming/comments/1ebw249/earth_defense_force_6_start_with_only_17_postive/",
    "https://www.reddit.com/gallery/1baks6k",
    "https://www.reddit.com/r/Sub4Sub/comments/1fdit4t/age_of_mythology_retold_global_illumination/",
    "https://www.reddit.com/r/unrealengine/comments/15sqto6/disadvantages_of_unreal_engine/",
    "https://www.reddit.com/r/unrealengine/comments/1i1a08l/anyone_else_still_on_unreal_engine_427_and_havent/",   
    "https://www.reddit.com/r/darksouls/comments/13j97co/i_put_dark_souls_anor_londo_into_the_unreal/",
    "https://www.reddit.com/r/videogames/comments/17owbdy/mark_my_words_photorealistic_graphics_will_happen/",     
    "https://www.reddit.com/r/HelpMeFind/comments/1hh96ua/2d_frog_game_with_photorealistic_graphics/",
    "https://www.reddit.com/r/steelseries/comments/1gnjkte/unreal_editor_for_fortnite_getting_detected/",
    "https://www.reddit.com/r/Youtubesubscribers/comments/1fditur/age_of_mythology_retold_global_illumination/",   
    "https://www.reddit.com/r/gamedev/comments/1hk8xf4/getting_unreal_editor_1_to_work_on_windows_xp/",
    "https://www.reddit.com/r/Fallout/comments/1hryr0x/fallout_4_has_been_one_of_the_most_immersive/",
    "https://www.reddit.com/r/augmentedreality/comments/y1qnja/unreal_engine_ar_apps_versus_webar_development/",   
    "https://www.reddit.com/gallery/1jna83y",
    "https://www.reddit.com/gallery/1hs3vce",
    "https://www.reddit.com/r/CryptoCurrency/comments/dhn4yz/nano_plugin_for_unreal_engine_4_is_now_available/",   
    "https://www.reddit.com/r/unrealengine/comments/1cw4hmv/unreal_engine_5_whenever_i_try_to_create_a_class/",    
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/hfiamt/the_initiatives_game_is_actionadventure_with/",
    "https://www.reddit.com/r/OculusQuest/comments/1c7usbo/i_was_featured_prominently_as_one_of_the_best_180/",    
    "https://www.reddit.com/r/SteamDeck/comments/1fi66gc/best_way_to_play_epic_games/",
    "https://www.reddit.com/gallery/jriou5",
    "https://www.reddit.com/r/GamingLeaksAndRumours/comments/1fzws7u/halo_infinite_2_was_in_development_using/",   
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
