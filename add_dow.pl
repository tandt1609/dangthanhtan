#!/usr/bin/env perl
use strict;
use warnings;
use utf8;
use open ':std', ':encoding(UTF-8)';

my $source_file = '../file for wed/charles-dow-tong-hop.html';
my $index_file  = 'index.html';

print "Reading $source_file...\n";
open my $sf, '<:encoding(UTF-8)', $source_file or die "Cannot open $source_file: $!";
my $source_html = do { local $/; <$sf> };
close $sf;

# 1. Extract <style>
my ($style_content) = $source_html =~ m{<style>(.*?)</style>}s;
die "No <style> found in source" unless defined $style_content;

# Scope CSS
$style_content =~ s{:root\b}{&}g;
$style_content =~ s{\bbody\s*\{}{&.dow-body \{}g;
$style_content =~ s{\bhtml\s*\{}{&.dow-html \{}g;

my $scoped_style = <<"CSS";
<style>
#article-dow-panel {
$style_content
}
</style>
CSS

# 2. Extract <body>
my ($body_content) = $source_html =~ m{<body>(.*?)</body>}s;
die "No <body> found in source" unless defined $body_content;

my $panel_html = <<"HTML";
<div id="article-dow-panel" class="sukien-article-panel dow-body">
$scoped_style
    <div style="padding: 16px 20px; background: #e1e9ec;">
        <button class="back-btn" onclick="openLegendArticle('')" style="color: #0e2a3f; border: 1px solid #c3d0d5; padding: 7px 16px; cursor: pointer; background: #f0f4f5; font-family: inherit; font-size: 0.95rem; border-radius: 4px; font-weight: 600;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
$body_content
    <div style="padding: 20px; text-align: center; background: #e1e9ec;">
        <button class="back-btn" onclick="openLegendArticle('')" style="color: #0e2a3f; border: 1px solid #c3d0d5; padding: 7px 16px; cursor: pointer; background: #f0f4f5; font-family: inherit; font-size: 0.95rem; border-radius: 4px; font-weight: 600;">
            <i class="fa-solid fa-arrow-left"></i> Quay lại danh sách
        </button>
    </div>
</div>
HTML

# 3. Read index.html
print "Reading $index_file...\n";
open my $inf, '<:encoding(UTF-8)', $index_file or die "Cannot open $index_file: $!";
my $index_html = do { local $/; <$inf> };
close $inf;

# A. Add Google Fonts if not present
my $font_tag = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Be+Vietnam+Pro:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">';
if ($index_html !~ /family=Fraunces/) {
    $index_html =~ s{(<link href="https://fonts\.googleapis\.com/css2\?family=Space\+Mono:[^"]+" rel="stylesheet">)}{$1\n    $font_tag};
    if ($index_html !~ /family=Fraunces/) {
        $index_html =~ s{(<link href="https://fonts\.googleapis\.com/css2\?family=Bricolage\+Grotesque:[^"]+" rel="stylesheet">)}{$1\n    $font_tag};
    }
    print "Added Fraunces & Be Vietnam Pro Google fonts\n";
}

# B. Insert card into Trang Chu (Home) news-list
my $home_card = <<"HCARD";
                        <!-- Post: Charles Dow (Huyen Thoai) -->
                        <a href="/huyen-thoai/charles-dow" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-crown"></i> Huyền thoại &amp; Thị trường</span>
                                <span class="news-time">19/09/2026</span>
                            </div>
                            <h3 class="news-heading">Charles Dow — Ông Nhà Báo Đo Thủy Triều Cho Phố Wall</h3>
                            <p class="news-excerpt">Người sáng lập The Wall Street Journal, cha đẻ chỉ số Dow Jones và người đặt nền móng đầu tiên cho toàn bộ ngành phân tích kỹ thuật hiện đại.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>
HCARD

if ($index_html !~ /id="panel-trang-chu".*?href="\/huyen-thoai\/charles-dow"/s) {
    # Insert at top of news-list in panel-trang-chu
    $index_html =~ s{(<div id="panel-trang-chu" class="tab-panel active">\s*<h2 class="section-title"><i class="fa-solid fa-fire-flame-curved"></i> Bài viết mới</h2>\s*<div class="news-list">)}{$1\n$home_card}s;
    print "Added card to Trang Chu (Home)\n";
} else {
    print "Card already exists in Trang Chu\n";
}

# C. Insert card into Huyen Thoai news-list
my $ht_card = <<"HTCARD";
                        <!-- Post: Charles Dow -->
                        <a href="/huyen-thoai/charles-dow" class="news-card clickable-card">
                            <div class="news-meta">
                                <span class="news-source"><i class="fa-solid fa-crown"></i> Phân tích kỹ thuật &amp; Chỉ số</span>
                                <span class="news-time">06/11/1851 – 04/12/1902</span>
                            </div>
                            <h3 class="news-heading"><span style="font-size:0.75em;color:#6fae6a;font-weight:500;display:block;margin-bottom:2px;letter-spacing:0.04em;">Phân tích kỹ thuật &amp; Thị trường</span>Charles Dow — Ông Nhà Báo Đo Thủy Triều Cho Phố Wall</h3>
                            <p class="news-excerpt">Người sáng lập The Wall Street Journal, cha đẻ chỉ số Dow Jones và người đặt nền móng đầu tiên cho toàn bộ ngành phân tích kỹ thuật hiện đại.</p>
                            <div class="news-footer">
                                <span class="sentiment-indicator bullish"><i class="fa-solid fa-book-open"></i> Đọc hồ sơ</span>
                            </div>
                        </a>
HTCARD

if ($index_html !~ /id="panel-huyen-thoai".*?href="\/huyen-thoai\/charles-dow"/s) {
    my $ht_target = '<!-- Post: Edward Thorp -->';
    if ($index_html =~ /\Q$ht_target\E/) {
        $index_html =~ s{\Q$ht_target\E}{$ht_card\n$ht_target};
        print "Added card to Huyen Thoai\n";
    } else {
        $index_html =~ s{(<div id="panel-huyen-thoai"[^>]*>.*?<div class="news-list">)}{$1\n$ht_card}s;
        print "Added card to Huyen Thoai (fallback)\n";
    }
} else {
    print "Card already exists in Huyen Thoai\n";
}

# D. Insert article panel
if ($index_html !~ /id="article-dow-panel"/) {
    my $panel_target = '</div><!-- /#huyen-thoai-article-view -->';
    if ($index_html =~ /\Q$panel_target\E/) {
        $index_html =~ s{\Q$panel_target\E}{$panel_html\n$panel_target};
        print "Added article-dow-panel\n";
    } else {
        die "Could not find panel target: $panel_target\n";
    }
} else {
    print "Panel already exists in index.html\n";
}

# Write index.html
open my $outf, '>:encoding(UTF-8)', $index_file or die "Cannot write $index_file: $!";
print $outf $index_html;
close $outf;
print "Successfully updated $index_file!\n";
