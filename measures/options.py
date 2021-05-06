import os, glob

external_libraries = ["--with%s" % p for p in ("-select_module",
                                                "-poll_module",
                                                "-threads",
                                                "-file-aio",
                                                "-http_ssl_module",
                                                "-http_v2_module",
                                                "-http_realip_module",
                                                "-http_addition_module",
                                                "-http_xslt_module",
                                                "-http_xslt_module=dynamic",
                                                "-http_image_filter_module",
                                                "-http_image_filter_module=dynamic",
                                                "-http_geoip_module",
                                                "-http_geoip_module=dynamic",
                                                "-http_sub_module",
                                                "-http_dav_module",
                                                "-http_flv_module",
                                                "-http_mp4_module",
                                                "-http_gunzip_module",
                                                "-http_gzip_static_module",
                                                "-http_auth_request_module",
                                                "-http_random_index_module",
                                                "-http_secure_link_module",
                                                "-http_degradation_module",
                                                "-http_slice_module",
                                                "-http_stub_status_module",
                                                # "-http_perl_module", # It shows an error during make
                                                "-http_perl_module=dynamic",
                                                "-mail",
                                                "-mail=dynamic",
                                                "-mail_ssl_module",
                                                "-stream",
                                                "-stream=dynamic",
                                                "-stream_ssl_module",
                                                "-stream_realip_module",
                                                "-stream_geoip_module",
                                                "-stream_geoip_module=dynamic",
                                                "-stream_ssl_preread_module",
                                                "-google_perftools_module",
                                                # "-cpp_test_module", # an error in code is shown!
                                                "-compat",
                                                "-pcre",
                                                "-pcre-jit",
                                                "-zlib-asm=CPU",
                                                "-libatomic",
                                                "-debug",
                                                "-openssl=/usr/bin"
                                            )]

external_libraries_2 = ["--without%s" % p for p in ("-select_module",
                                                    "-poll_module",
                                                    "-http_charset_module",
                                                    "-http_gzip_module",
                                                    "-http_ssi_module",
                                                    "-http_userid_module",
                                                    "-http_access_module",
                                                    "-http_auth_basic_module",
                                                    "-http_mirror_module",
                                                    "-http_autoindex_module",
                                                    "-http_geo_module",
                                                    "-http_map_module",
                                                    "-http_split_clients_module",
                                                    "-http_referer_module",
                                                    "-http_rewrite_module",
                                                    "-http_proxy_module",
                                                    "-http_fastcgi_module",
                                                    "-http_uwsgi_module",
                                                    "-http_scgi_module",
                                                    "-http_grpc_module",
                                                    "-http_memcached_module",
                                                    "-http_limit_conn_module",
                                                    "-http_limit_req_module",
                                                    "-http_empty_gif_module",
                                                    "-http_browser_module",
                                                    "-http_upstream_hash_module",
                                                    "-http_upstream_ip_hash_module", 
                                                    "-http_upstream_least_conn_module", 
                                                    "-http_upstream_random_module",
                                                    "-http_upstream_keepalive_module",
                                                    "-http_upstream_zone_module",
                                                    "-http",
                                                    "-http-cache",
                                                    "-mail_pop3_module",
                                                    "-mail_imap_module",
                                                    "-mail_smtp_module",
                                                    "-stream_limit_conn_module",
                                                    "-stream_access_module",
                                                    "-stream_geo_module",
                                                    "-stream_map_module",
                                                    "-stream_split_clients_module",
                                                    "-stream_return_module",
                                                    "-stream_upstream_hash_module",
                                                    "-stream_upstream_least_conn_module",
                                                    "-stream_upstream_random_module",
                                                    "-stream_upstream_zone_module",
                                                    #"-pcre" # The library is requited, is installed, it depends from the http!   
                                            )]


all_options = []

# Adding the single configurations to an array 
def extractDigits(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
    #print(res)
    return(res)
   

# All single configurations                   
single_configurations_01 = extractDigits(external_libraries)
single_configurations_02 = extractDigits(external_libraries_2)

# Adding the sample configuration sets (generated by FeatureIDE) to an array
sample_configurations = []

for variant in glob.glob("measures/products_2-200/*.config"):
    lineList = list()
    with open(variant) as f:
        for line in f:
            lineList = [line.rstrip('\n') for line in open(variant)]
        sample_configurations.append(lineList)

#print(sample_configurations)
#print(*single_configurations_01,*single_configurations_02)

# All single and sample configurations, 
# which will be used to measure the changes on
# the binary size and number of gadgets in x264
all_options =  [*sample_configurations]